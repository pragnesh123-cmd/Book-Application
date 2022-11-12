from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
import models


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/get_all_address_books/")
def get_all_address_books(db: Session = Depends(get_db)):
    return crud.get_all_address_books(db)


@app.get("/get_single_address_books/{id}")
def get_single_address_books(address_books_id: int, db: Session = Depends(get_db)):
    return crud.get_single_address_books(db,address_books_id)


@app.delete("/delete_address_books/{id}")
def delete_address_books(address_books_id: int, db: Session = Depends(get_db)):
    return crud.delete_address_book(db,address_books_id)


@app.post("/create_address_book/")
def create_item_for_user(
    item: schemas.AddressCreate, db: Session = Depends(get_db)
):
    return crud.create_addressbook(db=db, item=item)


@app.put("/update_address_book/{id}")
def update_address_book(address_book_id: int,item: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.update_address_book(db,item=item,address_book_id=address_book_id)
