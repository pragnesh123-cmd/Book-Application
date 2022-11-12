from sqlalchemy.orm import Session
import models, schemas
import requests

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
    url = f"https://api.geoapify.com/v1/geocode/search?text={item.address}&type=city&format=json&apiKey=1fbc2f263ab342f2b40c9f17ae2c9f2d"
    response = requests.get(url)
    r = response.json()
    long = r.get("results")[0].get("lon")
    lat = r.get("results")[0].get("lat")
    db_user = models.AddressBook(address=item.address,lat=lat,long=long)
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