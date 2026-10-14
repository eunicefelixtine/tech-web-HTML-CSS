# Technologies Web et Applications — TP1 à TP6

## Présentation du projet

Ce dépôt regroupe les travaux pratiques (TP1 à TP6) réalisés dans le cadre du cours de Technologies Web et Applications. Ces travaux permettent de découvrir progressivement les technologies du développement web, de la création de pages HTML à la réalisation d’une application web dynamique avec Python et Flask.

## Objectifs pédagogiques

Les différents TP ont pour objectifs de :

- Comprendre la structure d’une page web et utiliser les principales balises HTML.
- Mettre en forme les pages avec CSS et créer des interfaces adaptées aux différentes tailles d’écran.
- Utiliser JavaScript pour rendre les pages interactives, manipuler le DOM et contrôler les formulaires.
- Organiser les fichiers d’un projet web en séparant le contenu, la présentation et les comportements.
- Découvrir le développement côté serveur avec Flask et Python.
- Créer et manipuler une base de données SQLite pour stocker et récupérer des informations.
- Mettre en place des formulaires, des routes, des gabarits HTML et une API renvoyant des données au format JSON.
- Appliquer les bonnes pratiques de sécurité lors de la validation et du traitement des données.

## Technologies utilisées

- **HTML5** : structure et contenu des pages web.
- **CSS3** : présentation, mise en forme et adaptation des interfaces.
- **JavaScript** : interactions, manipulation du DOM, validation des formulaires et récupération de données.
- **Python** : programmation de la partie serveur.
- **Flask** : création des routes et gestion des requêtes HTTP.
- **SQLite** : stockage et gestion des données.
- **Jinja2** : génération des pages HTML à partir de gabarits.
- **Visual Studio Code** : édition et organisation du code.

## Organisation générale

Les fichiers sont organisés selon les besoins de chaque TP. Pour l’application Flask du TP6, l’organisation est la suivante :

```text
restaurant_flask_tp6/
├── app.py
├── schema.sql
├── restaurant.db
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── menu.html
│   ├── reserver.html
│   └── reservations.html
└── static/
    ├── style.css
    ├── script.js
    └── images/
```

- `app.py` contient les routes Flask et la logique de traitement côté serveur.
- `schema.sql` définit la structure de la base de données et les données initiales.
- `restaurant.db` est la base de données SQLite créée par l’application.
- `templates/` contient les gabarits HTML.
- `static/` contient les fichiers CSS, JavaScript et les images.

## Présentation des travaux pratiques

### TP1 à TP4 — Bases du développement web

Ces travaux pratiques permettent de se familiariser avec les technologies fondamentales du Web, notamment la structure des pages HTML, leur mise en forme avec CSS et l’organisation des éléments d’une interface.

### TP5 — Interactivité avec JavaScript

Ce TP permet d’approfondir la programmation côté client, notamment la sélection des éléments HTML, la gestion des événements, le contrôle des formulaires et la récupération de données avec `fetch()`. Il met également l’accent sur la manipulation sécurisée du contenu des pages.

### TP6 — Développement d’une application avec Flask

Ce TP consiste à développer une application web de restaurant. Il permet de créer des routes Flask, d’utiliser des gabarits Jinja2, de gérer une base de données SQLite, d’enregistrer et d’annuler des réservations, ainsi que de fournir les données du menu au format JSON à travers une API. Il aborde également la validation des données et les principales précautions de sécurité.

## Installation et exécution du TP6

### 1. Créer un environnement virtuel

```bash
python3 -m venv .venv
```

### 2. Activer l’environnement virtuel

Sous Linux :

```bash
source .venv/bin/activate
```

### 3. Installer Flask

```bash
pip install flask
```

### 4. Lancer l’application

```bash
python app.py
```

Ouvrir ensuite l’adresse suivante dans un navigateur :

http://127.0.0.1:5000

## Sécurité et bonnes pratiques

Les travaux pratiques abordent plusieurs bonnes pratiques du développement web :

- Valider les données saisies par l’utilisateur côté client et côté serveur.
- Utiliser des requêtes SQL paramétrées pour limiter les risques d’injection SQL.
- Privilégier `textContent` pour afficher du texte utilisateur sans l’interpréter comme du HTML.
- Organiser les fichiers pour faciliter la maintenance du projet.
- Désactiver le mode débogage de Flask en environnement de production.

## Conclusion

La réalisation des TP1 à TP6 permet d’acquérir des bases progressives en développement web, depuis la création d’interfaces statiques jusqu’à la conception d’une application dynamique reliée à une base de données. L’ensemble de ces travaux contribue à comprendre le fonctionnement des technologies côté client et côté serveur, ainsi que l’importance de l’organisation du code, de la validation des données et de la sécurité des applications web.

TP réalisé par NZEUTEM DOMMOE Eunice Felixtine - 22G00347