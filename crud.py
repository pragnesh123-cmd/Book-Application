from sqlalchemy.orm import Session
import models, schemas


def get_all_address_books(db: Session):
    return db.query(models.AddressBook).all()

def get_single_address_books(db: Session,address_book_id:id):
    address_book = db.query(models.AddressBook).get(address_book_id)
    if address_book:
        return address_book
    else: 
        return{
       "code":"success",
       "message":"address book is does not exists."
    }

def create_addressbook(db: Session,item: schemas.AddressCreate):
    db_user = models.AddressBook(address=item.address,lat=item.lat,long=item.long)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_address_book(db: Session,item:schemas.AddressCreate,address_book_id:int):
    address_book = db.query(models.AddressBook).get(address_book_id)
    address_book.address = item.address
    address_book.lat = item.lat
    address_book.long = item.long
    db.add(address_book)
    db.commit() 
    return{
       "code":"success",
       "message":"address book updated successfully."
    }

def delete_address_book(db: Session,address_book_id:int):
    address_book = db.query(models.AddressBook).get(address_book_id)
    if address_book is None:
        return  {"code":"Success","message":"address book is not exits."}
    db.delete(address_book)
    db.commit()
    return {"code":"Success","message":"address book deleted successfully."}