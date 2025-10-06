from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Cette classe charge et valide les variables d'environnement.
    Elle lira automatiquement le fichier .env pour nous.
    """
    DB_HOSTNAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str

    # Indique à Pydantic de chercher un fichier .env
    model_config = SettingsConfigDict(env_file="/Users/wassim/Desktop/book-scraper/project_book_scraper/.env")

# On crée une instance unique de nos paramètres que nous utiliserons dans toute l'application
settings = Settings()