
from sqlalchemy.orm import Session
from sqlalchemy import text



def get_book_by_id(db: Session, book_id: int):
    """
    Récupère un livre de la base de données par son ID.

    :param db: La session de base de données (fournie par notre dépendance get_db).
    :param book_id: L'ID du livre à rechercher.
    """
    # On écrit notre requête SQL avec un paramètre nommé ':id' pour la sécurité
    sql_query = text("SELECT * FROM books WHERE id = :id;")

    # On exécute la requête en passant la valeur du paramètre
    result = db.execute(sql_query, {"id": book_id}).first()

    return result


def get_all_books(db: Session, skip: int = 0, limit: int = 100):
    """
    Récupère une liste de livres avec pagination.

    :param db: La session de base de données.
    :param skip: Le nombre de livres à sauter (pour la pagination, équivalent à OFFSET).
    :param limit: Le nombre maximum de livres à retourner.
    """
    sql_query = text("SELECT * FROM books ORDER BY id LIMIT :limit OFFSET :skip;")

    results = db.execute(sql_query, {"limit": limit, "skip": skip}).all()

    return results