from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings

# On charge les variables d'environnement du fichier .env
load_dotenv()


# On construit l'URL de connexion standard pour PostgreSQL
DATABASE_URL = (
    f"postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOSTNAME}/{settings.DB_NAME}"
)

# --- Moteur et Session SQLAlchemy ---


engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# --- Dépendance FastAPI ---

def get_db():
    """
    Cette fonction est une "dépendance" FastAPI.
    À chaque requête entrante, elle va :
    1. Créer une nouvelle session de base de données.
    2. Fournir cette session à la requête (avec 'yield').
    3. S'assurer que la session est bien fermée à la fin (même en cas d'erreur).
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()