import re
import sqlite3
from datetime import date
from pathlib import Path

from flask import (
    Flask, render_template, request, redirect,
    url_for, flash, g, jsonify
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "changez-moi"  # À remplacer en production

BASE = Path(app.root_path) / "restaurant.db"
SCHEMA = Path(app.root_path) / "schema.sql"


# ---------- Connexion à la base de données ----------

def get_db():
    """Ouvre une connexion par requête et la réutilise pendant cette requête."""
    if "db" not in g:
        g.db = sqlite3.connect(BASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def fermer_db(exception):
    """Ferme la connexion à la fin de la requête."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


# ---------- Initialisation de la base ----------

def init_db():
    """Crée les tables à partir du fichier schema.sql."""
    with app.app_context():
        db = get_db()
        with open(SCHEMA, encoding="utf-8") as fichier:
            db.executescript(fichier.read())
        db.commit()


# ---------- Pages ----------

@app.route("/")
def accueil():
    return render_template("index.html")


@app.route("/menu")
def menu():
    plats = get_db().execute(
        "SELECT nom, categorie, prix FROM plats ORDER BY categorie, prix"
    ).fetchall()
    return render_template("menu.html", plats=plats)


# ---------- Réservations ----------

@app.route("/reserver", methods=["GET", "POST"])
def reserver():
    if request.method == "POST":
        nom = request.form.get("nom", "").strip()
        tel = re.sub(r"\s+", "", request.form.get("telephone", ""))
        jour = request.form.get("date", "")
        service = request.form.get("service", "")
        personnes = request.form.get("personnes", "")

        erreurs = []

        if not nom:
            erreurs.append("Le nom est obligatoire.")

        if not re.fullmatch(r"6\d{8}", tel):
            erreurs.append(
                "Numéro invalide : 9 chiffres commençant par 6."
            )

        if service not in ("midi", "soir"):
            erreurs.append("Service inconnu.")

        if not personnes.isdigit() or not 1 <= int(personnes) <= 20:
            erreurs.append(
                "Le nombre de personnes doit être entre 1 et 20."
            )

        try:
            date_reservation = date.fromisoformat(jour)
            if date_reservation < date.today():
                erreurs.append("La date est déjà passée.")
        except (ValueError, TypeError):
            erreurs.append("Date invalide.")

        if erreurs:
            for erreur in erreurs:
                flash(erreur, "erreur")
            return render_template(
                "reserver.html",
                donnees=request.form,
                date_min=date.today().isoformat()
            ), 400

        db = get_db()
        db.execute(
            """
            INSERT INTO reservations
                (nom, telephone, date, service, personnes)
            VALUES (?, ?, ?, ?, ?)
            """,
            (nom, tel, jour, service, int(personnes))
        )
        db.commit()

        flash(
            f"Merci {nom}, votre table est réservée pour le {jour} ({service}).",
            "succes"
        )
        return redirect(url_for("reserver"))

    return render_template(
        "reserver.html",
        donnees={},
        date_min=date.today().isoformat()
    )


@app.route("/reservations")
def reservations():
    lignes = get_db().execute(
        "SELECT * FROM reservations ORDER BY date, service"
    ).fetchall()
    return render_template("reservations.html", reservations=lignes)


@app.route("/reservations/<int:id_resa>/annuler", methods=["POST"])
def annuler(id_resa):
    db = get_db()
    resultat = db.execute(
        "DELETE FROM reservations WHERE id = ?", (id_resa,)
    )
    db.commit()

    if resultat.rowcount:
        flash("Réservation annulée.", "succes")
    else:
        flash("Réservation introuvable.", "erreur")

    return redirect(url_for("reservations"))


# ---------- API JSON ----------

@app.route("/api/menu")
def api_menu():
    plats = get_db().execute(
        "SELECT nom, categorie, prix FROM plats ORDER BY categorie, prix"
    ).fetchall()
    return jsonify([dict(plat) for plat in plats])


if __name__ == "__main__":
    if not BASE.exists():
        init_db()
    app.run(debug=True)
