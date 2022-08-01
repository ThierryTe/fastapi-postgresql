from sqlalchemy.orm import Session
from model import Book
from schemas import BookSchema

#Obtenir la liste de tous les livres
def get_book(db:Session,skip:int=0,limit:int=100):
    return db.query(Book).offset(skip).limit(limit).all()


#Afficher un livre par son id
def get_book_by_id(db:Session, book_id:int):
    return db.query(Book).filter(Book.id==book_id).first()


#Créer un livre
def create_book(db:Session,book:BookSchema):
    _book = Book(title=book.title,description=book.description)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book

#Supprimer un livre
def remove_book(db:Session, book_id:int):
    _book = get_book_by_id(db=db,book_id=book_id)
    db.delete(_book)
    db.commit()

#Mettre à jour un livre
def update_book(db:Session,book_id:int,title:str,description:str):
    _book = get_book_by_id(db=db,book_id=book_id)
    _book.title=title
    _book.description = description
    db.commit()
    db.refresh(_book)
    return _book