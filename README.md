# R5C4 — Données décisionnelles

Projet réalisé dans le cadre du BUT Informatique.

## Présentation

Ce projet consiste à construire un outil d'analyse de données
autour de données de parties de jeux vidéo.

L'application est composée de deux parties :

- une API REST développée avec Flask ;
- un tableau de bord développé avec Streamlit.

## Technologies

- Python
- Flask
- Streamlit
- SQLite
- Git / GitHub

## Architecture

### API Flask

L'API suit une architecture en couches :

- Controller
- Service
- Repository
- DTO

### Tableau de bord Streamlit

Le tableau de bord permet notamment :

- de consulter les parties ;
- de filtrer les données ;
- de naviguer entre les pages ;
- de visualiser des statistiques.

## Données

Les données sont issues de `parties.db`.

La base contient notamment les tables :

- `parties`
- `files`
- `jeux`
- `serveurs`

## Avancement

### Séance 1

- Mise en place du projet Flask
- Connexion à la base SQLite
- Mise en place de l'architecture Controller / Service / Repository / DTO
- Création de `GET /api/v1/parties`
- Ajout de la pagination avec `limit` et `offset`
- Ajout du nombre total de parties

### Séance 3

- Mise en place du tableau de bord Streamlit
- Navigation entre les pages
- Chargement des données
- Mise en cache des données
- Filtre par serveur
- Pagination des parties
- Première visualisation statistique
- Première réflexion sur les indicateurs du tableau de bord

## Installation

Créer un environnement virtuel :

```bash
python -m venv .venv
```

Activer l'environnement virtuel puis installer les dépendances :

```bash
pip install Flask Streamlit
```

## Lancement

### API Flask

```bash
python app.py
```

### Dashboard Streamlit

```bash
streamlit run streamlit_app.py
```

