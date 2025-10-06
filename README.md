# 📚 Projet de Web Scraping et API de Livres

Ce projet est une application **Python complète** qui réalise un **pipeline de données de bout en bout** : de la collecte de données sur un site web jusqu'à leur exposition via une API RESTful, en passant par le nettoyage et le stockage dans une base de données cloud.

Le site cible pour le scraping est **Books to Scrape**, un site de e-commerce factice conçu pour l'entraînement au web scraping.

---

## 🚀 Fonctionnalités

- **Scraping Complet** : Un spider développé avec *Scrapy* pour crawler l'intégralité du catalogue de 1000 livres sur 50 pages.  
- **Nettoyage Automatisé** : Une pipeline de données robuste qui nettoie et formate les informations collectées (prix, notes en étoiles, stock, etc.) en temps réel.  
- **Stockage Cloud** : Les données propres sont stockées dans une base de données **PostgreSQL** hébergée sur **Microsoft Azure**.  
- **Analyse de Données** : Un script d'analyse (`analysis.py`) pour exécuter des requêtes SQL complexes et extraire des statistiques (ex: prix moyen par catégorie, livres les mieux notés).  
- **API RESTful** : Une API performante construite avec *FastAPI* pour exposer les données au format JSON, en suivant les principes de la **Clean Architecture**.  
- **Gestion Sécurisée des Secrets** : Les identifiants de la base de données sont gérés de manière sécurisée grâce à un fichier `.env` et ne sont pas exposés dans le code source.  

---

## 🏛️ Architecture du Projet

Le projet est divisé en deux composants principaux : **le Scraper** et **l'API**.

### 🕷️ Scraper (Scrapy)
Le scraper est un projet Scrapy standard qui contient :  
- Un spider (`books.py`) pour la logique de crawling et d'extraction.  
- Des items (`items.py`) pour définir la structure des données et la logique de nettoyage via des processeurs.  
- Une pipeline (`pipelines.py`) pour gérer le stockage des données dans la base de données.  

### ⚙️ API (FastAPI)
L'API suit les principes de la **Clean Architecture** pour une séparation claire des responsabilités :  
- `main.py` (**Couche API**) : Définit les routes et gère les requêtes HTTP.  
- `services.py` (**Couche Service**) : Contient la logique métier.  
- `repositories.py` (**Couche Dépôt**) : Communique directement avec la base de données via SQL.  
- `schemas.py` (**Couche Schéma**) : Définit la forme des données avec *Pydantic*.  
- `database.py` & `config.py` : Gèrent la connexion à la base de données et la configuration.  

---

## 🛠️ Technologies Utilisées

| Catégorie | Technologies |
|------------|---------------|
| Langage | Python 3.11+ |
| Web Scraping | Scrapy |
| Base de Données | Azure Database for PostgreSQL |
| API | FastAPI, Uvicorn |
| ORM / SQL | SQLAlchemy, psycopg2-binary |
| Validation | Pydantic |
| Secrets | python-dotenv |

---

## ⚙️ Installation et Configuration

### 1. Prérequis
- Python 3.11 (ou une version stable de Python 3)  
- Un compte Microsoft Azure avec une base **Azure Database for PostgreSQL** configurée.

### 2. Cloner le Dépôt
```bash
git clonehttps://github.com/shini559/book-scraper.git
cd <nom_du_dossier_projet>
```

### 3. Configurer l’Environnement Virtuel
```bash
python3.11 -m venv .venv
source .venv/bin/activate
# Sur Windows : .\.venv\Scripts\activate
```

### 4. Installer les Dépendances
```bash
pip install -r requirements.txt
```

### 5. Configurer les Variables d’Environnement
Créez un fichier nommé `.env` à la racine du projet :  
```ini
DB_HOSTNAME=votre_serveur.postgres.database.azure.com
DB_USERNAME=votre_utilisateur
DB_PASSWORD=votre_mot_de_passe_encodé
DB_NAME=postgres
```

---

## 🚀 Utilisation

### 1. Lancer le Scraper
```bash
cd project_book_scraper
scrapy crawl books
```

### 2. Lancer les Analyses SQL
```bash
python analysis.py
```

### 3. Lancer l’API
```bash
uvicorn api.main:app --reload
```
API accessible sur : [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Documentation Swagger : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📈 Améliorations Possibles

- Déployer l’API sur Azure App Service  
- Ajouter des endpoints CRUD (POST, PUT, DELETE)  
- Mettre en place une authentification sécurisée  
- Containeriser avec Docker  
- Créer un front-end (React / Vue.js) pour consommer l’API  

---

## 📄 Licence

Ce projet est distribué sous la licence **MIT**.
