from pydantic import BaseModel

class Book(BaseModel):
    """
    Ce schéma Pydantic définit la structure des données d'un livre
    lorsqu'il est renvoyé par notre API.
    """
    id: int
    title: str
    price: float
    stock: int
    rating: int
    category: str
    description: str

    # --- Configuration pour la compatibilité avec SQLAlchemy ---
    class Config:
        """
        Cette petite configuration (anciennement 'orm_mode') indique à Pydantic
        qu'il doit lire les données même si elles ne proviennent pas d'un dictionnaire Python,
        mais d'un objet de base de données (comme les objets que SQLAlchemy nous donnera).
        """
        from_attributes = True