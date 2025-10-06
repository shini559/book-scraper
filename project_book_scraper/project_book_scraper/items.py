import scrapy
from itemloaders.processors import TakeFirst, MapCompose
import re


## --- Nos fonctions de nettoyage --- ##

def clean_price(text):
    """
    Extrait le nombre (entier ou à virgule) d'une chaîne de caractères.

    """

    match = re.findall(r'[\d.]+', text)
    if match:
        return float(match[0])
    return text


def clean_stock(text):
    """
    Extrait le nombre de livres en stock.
    """
    match = re.findall(r'\d+', text)
    if match:
        return int(match[0])
    return text


def strip_text(text):
    """
    Supprime les espaces et les sauts de ligne au début et à la fin.
    """
    return text.strip()


def convert_rating_to_int(class_text):
    """
    Extrait la note textuelle ('One', 'Two') de la classe CSS
    et la convertit en chiffre (1, 2).
    """

    rating_text = class_text.split(' ')[1]

    ratings = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    # On retourne le chiffre correspondant au mot, ou 0 si on ne trouve rien.
    return ratings.get(rating_text, 0)



## --- Notre Item avec ses processeurs --- ##

class BookScraperItem(scrapy.Item):
    # Pour le titre, on enlève les espaces inutiles puis on prend la première valeur.
    title = scrapy.Field(
        input_processor=MapCompose(strip_text),
        output_processor=TakeFirst()
    )

    # Pour le prix, on applique notre fonction de nettoyage puis on prend la première valeur.
    price = scrapy.Field(
        input_processor=MapCompose(clean_price),
        output_processor=TakeFirst()
    )

    # Pour le stock on applique notre fonction de nettoyage puis on prend la première valeur.
    stock = scrapy.Field(
        input_processor=MapCompose(clean_stock),
        output_processor=TakeFirst()
    )

    # Pour la description, on enlève juste les espaces.
    description = scrapy.Field(
        input_processor=MapCompose(strip_text),
        output_processor=TakeFirst()
    )

    # Pour la note on convertie en chiffre
    rating = scrapy.Field(
        input_processor=MapCompose(convert_rating_to_int),
        output_processor=TakeFirst()
    )
    # Les catégorie
    category = scrapy.Field(
        input_processor=MapCompose(strip_text),
        output_processor=TakeFirst()
    )