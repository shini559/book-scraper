
import os
import psycopg2
from dotenv import load_dotenv

print("Tentative de connexion à la base de données Azure...")

# On charge les variables du fichier .env
load_dotenv()

try:
    # On essaie de se connecter en utilisant les variables d'environnement
    conn = psycopg2.connect(
        host=os.getenv('DB_HOSTNAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        dbname=os.getenv('DB_NAME')
    )

    print("✅ Connexion à la base de données Azure réussie !")

    # On referme la connexion
    conn.close()

except psycopg2.Error as e:
    print("❌ Échec de la connexion.")
    print(f"L'erreur suivante s'est produite : {e}")