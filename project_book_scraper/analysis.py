import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# --- DÉFINITION DE NOS FONCTIONS D'ANALYSE ---

def get_average_price_by_category(cursor):
    print("\n--- Analyse 1 : Prix Moyen par Catégorie ---")
    sql_query = """
        SELECT category, AVG(price) AS average_price
        FROM books
        GROUP BY category
        ORDER BY average_price DESC;
    """
    cursor.execute(sql_query)
    results = cursor.fetchall()
    for row in results:
        print(f"Catégorie: {row[0]:<25} | Prix Moyen: £{round(row[1], 2)}")

def get_top_five_categories_by_book_count(cursor):
    print("\n--- Analyse 2 : Top 5 des Catégories par Nombre de Livres ---")
    sql_query = """
        SELECT category, COUNT(id) AS book_count
        FROM books
        GROUP BY category
        ORDER BY book_count DESC
        LIMIT 5;
    """
    cursor.execute(sql_query)
    results = cursor.fetchall()
    for row in results:
        print(f"Catégorie: {row[0]:<25} | Nombre de livres: {row[1]}")

def get_top_rated_books(cursor):
    """Récupère les 10 livres avec la meilleure note."""
    print("\n--- Analyse 3 : Top 10 des Livres les Mieux Notés ---")
    sql_query = """
        SELECT title, rating, price FROM books
        ORDER BY rating DESC, price ASC
        LIMIT 10;
    """
    cursor.execute(sql_query)
    results = cursor.fetchall()
    for row in results:
        print(f"Note: {row[1]}/5 | Prix: £{row[2]:<6} | Titre: {row[0]}")

def get_average_rating_by_category(cursor):
    """Calcule la note moyenne pour chaque catégorie."""
    print("\n--- Analyse 4 : Classement des Catégories par Note Moyenne ---")
    sql_query = """
        SELECT category, AVG(rating) AS average_rating
        FROM books
        GROUP BY category
        ORDER BY average_rating DESC;
    """
    cursor.execute(sql_query)
    results = cursor.fetchall()
    for row in results:
        print(f"Note Moyenne: {round(row[1], 2):<4}/5 | Catégorie: {row[0]}")


# --- BLOC PRINCIPAL DE CONNEXION ET D'EXÉCUTION ---
conn = None
try:
    conn = psycopg2.connect(
        host=os.getenv('DB_HOSTNAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        dbname=os.getenv('DB_NAME')
    )
    cur = conn.cursor()
    print("✅ Connexion réussie ! Lancement des analyses.\n")

    # On appelle toutes nos fonctions d'analyse
    get_average_price_by_category(cur)
    get_top_five_categories_by_book_count(cur)
    get_top_rated_books(cur)
    get_average_rating_by_category(cur)

    cur.close()

except psycopg2.Error as e:
    print(f"❌ Erreur de base de données : {e}")

finally:
    if conn is not None:
        conn.close()
        print("\n\nConnexion à la base de données fermée.")