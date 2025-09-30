import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
conn = None

try:
    conn = psycopg2.connect(
        host=os.getenv('DB_HOSTNAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        dbname=os.getenv('DB_NAME')
    )
    cur = conn.cursor()
    print("✅ Connexion réussie !")

    # Requête spéciale pour lister toutes les tables dans le schéma public
    print("\nRecherche des tables existantes dans la base de données...")
    cur.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name;
                """)

    # On récupère toutes les lignes du résultat
    tables = cur.fetchall()

    if not tables:
        print("-> Aucune table trouvée dans la base de données.")
    else:
        print("-> Tables trouvées :")
        for table in tables:
            print(f"- {table[0]}")  # table[0] pour afficher le nom de la table

    cur.close()

except psycopg2.Error as e:
    print(f"❌ Erreur de base de données : {e}")

finally:
    if conn is not None:
        conn.close()
        print("\nConnexion à la base de données fermée.")