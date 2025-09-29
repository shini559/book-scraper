# Dans le fichier test_connection.py

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

    # Si la ligne ci-dessus n'a pas provoqué d'erreur, la connexion est réussie !
    print("✅ Connexion à la base de données Azure réussie !")

    # On referme la connexion proprement
    conn.close()

except psycopg2.Error as e:
    # Si une erreur se produit pendant la connexion, on l'affiche.
    print("❌ Échec de la connexion.")
    print(f"L'erreur suivante s'est produite : {e}")