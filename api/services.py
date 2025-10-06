from sqlalchemy.orm import Session
from . import repositories, schemas

def get_all_books(db: Session, skip: int = 0, limit: int = 100):
    """
    Service pour récupérer une liste de livres.
    Il appelle la fonction du dépôt correspondante.
    """

    return repositories.get_all_books(db=db, skip=skip, limit=limit)

def get_book_by_id(db: Session, book_id: int):
    """
    Service pour récupérer un livre par son ID.
    """
    return repositories.get_book_by_id(db=db, book_id=book_id)