from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# On importe toutes nos briques depuis les autres fichiers
from . import services, schemas, database

# On crée l'application FastAPI
app = FastAPI(
    title="Book Scraper API",
    description="Une API pour accéder aux données de livres scrapés.",
    version="1.0.0"
)

# --- Définition de nos Routes (Endpoints) ---

@app.get("/books/", response_model=List[schemas.Book], tags=["Books"])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    """
    Récupère une liste de livres avec pagination.
    """
    books = services.get_all_books(db, skip=skip, limit=limit)
    return books

@app.get("/books/{book_id}", response_model=schemas.Book, tags=["Books"])
def read_book(book_id: int, db: Session = Depends(database.get_db)):
    """
    Récupère un livre unique par son ID.
    """
    db_book = services.get_book_by_id(db, book_id=book_id)
    if db_book is None:
        # Si le livre n'est pas trouvé, on lève une exception HTTP 404
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book