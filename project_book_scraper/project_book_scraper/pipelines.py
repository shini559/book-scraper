import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class BookScraperPipeline:
    def __init__(self):
        print("🚀 Pipeline initialisée ! Tentative de connexion à la base de données...")
        hostname = os.getenv('DB_HOSTNAME')
        username = os.getenv('DB_USERNAME')
        password = os.getenv('DB_PASSWORD')
        database = os.getenv('DB_NAME')

        self.con = psycopg2.connect(
            host=hostname, user=username, password=password, dbname=database
        )
        self.cur = self.con.cursor()
        print("✅ Connexion à la base de données réussie.")
        self.create_table()

    def create_table(self):
        print("📝 Tentative de création de la table 'books'...")
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS books(
                id SERIAL PRIMARY KEY,
                title TEXT,
                price REAL,
                stock INTEGER,
                rating INTEGER,
                category TEXT,
                description TEXT
            )
        """)
        # On ajoute un commit ici pour s'assurer que la création est bien enregistrée
        self.con.commit()
        print("👍 La table 'books' est prête.")

    def process_item(self, item, spider):
        print(f"📥 Réception d'un item : {item['title']}")
        self.cur.execute(
            "INSERT INTO books (title, price, stock, rating, category, description) VALUES (%s, %s, %s, %s, %s, %s)",
            (
                item['title'], item['price'], item['stock'],
                item['rating'], item['category'], item['description']
            )
        )
        self.con.commit()
        print(f"💾 Item sauvegardé dans la base de données.")
        return item

    def close_spider(self, spider):
        print("🏁 Spider terminé. Fermeture de la connexion à la base de données.")
        self.con.close()