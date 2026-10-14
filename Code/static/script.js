// ---------- 1. Menu hamburger ----------
const boutonMenu = document.querySelector("#bouton-menu");
const nav = document.querySelector("header nav");

if (boutonMenu && nav) {
    boutonMenu.addEventListener("click", () => {
        const ouvert = nav.classList.toggle("ouvert");
        boutonMenu.setAttribute("aria-expanded", String(ouvert));
    });
}


// ---------- 2. Vérification du formulaire côté navigateur ----------
const form = document.querySelector("#form-reservation");

if (form) {
    const erreur = document.querySelector("#erreur");

    form.addEventListener("submit", (evenement) => {
        const messages = [];
        const nom = form.elements["nom"].value.trim();
        const tel = form.elements["telephone"].value.replace(/\s/g, "");
        const personnes = Number(form.elements["personnes"].value);
        const valeurDate = form.elements["date"].value;

        if (nom === "") {
            messages.push("Indiquez votre nom.");
        }

        if (!/^6\d{8}$/.test(tel)) {
            messages.push("Numéro invalide : 9 chiffres commençant par 6.");
        }

        if (!Number.isInteger(personnes) || personnes < 1 || personnes > 20) {
            messages.push("Le nombre de personnes doit être entre 1 et 20.");
        }

        if (!valeurDate) {
            messages.push("Choisissez une date.");
        } else {
            const aujourdHui = new Date();
            aujourdHui.setHours(0, 0, 0, 0);
            const dateChoisie = new Date(`${valeurDate}T00:00:00`);

            if (Number.isNaN(dateChoisie.getTime()) || dateChoisie < aujourdHui) {
                messages.push("Choisissez une date qui n'est pas passée.");
            }
        }

        erreur.textContent = messages.join(" ");

        if (messages.length > 0) {
            evenement.preventDefault();
        }
    });
}


// ---------- 3. Menu dynamique depuis l'API Flask ----------
const liste = document.querySelector("#liste-menu");
let tousLesPlats = [];

function categoriePourFiltre(categorie) {
    // Dans la base, la catégorie est écrite « entrée ».
    return categorie === "entrée" ? "entree" : categorie;
}

function afficherPlats(categorie) {
    if (!liste) return;

    liste.replaceChildren();

    const plats = categorie === "tout"
        ? tousLesPlats
        : tousLesPlats.filter(
            (plat) => categoriePourFiltre(plat.categorie) === categorie
        );

    if (plats.length === 0) {
        const li = document.createElement("li");
        li.textContent = "Aucun plat dans cette catégorie.";
        liste.appendChild(li);
        return;
    }

    for (const plat of plats) {
        const li = document.createElement("li");
        li.textContent = `${plat.nom} : ${plat.prix} FCFA`;
        li.dataset.categorie = categoriePourFiltre(plat.categorie);
        liste.appendChild(li);
    }
}

async function chargerMenu() {
    if (!liste) return;

    try {
        const reponse = await fetch("/api/menu");

        if (!reponse.ok) {
            throw new Error(`Erreur HTTP ${reponse.status}`);
        }

        tousLesPlats = await reponse.json();
        afficherPlats("tout");
    } catch (erreur) {
        liste.textContent = "Le menu est momentanément indisponible.";
        console.error("Erreur de chargement du menu :", erreur);
    }
}

if (liste) {
    chargerMenu();

    document.querySelectorAll(".filtre").forEach((bouton) => {
        bouton.addEventListener("click", () => {
            document.querySelectorAll(".filtre").forEach((element) => {
                element.classList.remove("actif");
            });
            bouton.classList.add("actif");
            afficherPlats(bouton.dataset.categorie);
        });
    });
}
