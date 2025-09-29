import psycopg2
import os
from dotenv import load_dotenv

class BookScraperPipeline:
    def __init__(self):
        hostname = os.getenv('DB_HOSTNAME')
        username = os.getenv('DB_USERNAME')
        password = os.getenv('DB_PASSWORD')
        database = os.getenv('DB_NAME')

        # Connexion à la base de données PostgreSQL
        self.con = psycopg2.connect(
            host=hostname,
            user=username,
            password=password,
            dbname=database
        )
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        # La syntaxe pour une clé primaire auto-incrémentée est un peu différente
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

    def process_item(self, item, spider):
        # La syntaxe pour les placeholders est '%s' au lieu de '?'
        self.cur.execute(
            "INSERT INTO books (title, price, stock, rating, category, description) VALUES (%s, %s, %s, %s, %s, %s)",
            (
                item['title'],
                item['price'],
                item['stock'],
                item['rating'],
                item['category'],
                item['description']
            )
        )
        self.con.commit()
        return item

    def close_spider(self, spider):
        self.con.close()