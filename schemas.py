from pydantic import BaseModel


class AddressBookBase(BaseModel):
    address: str
    lat: str
    long: str

class AddressCreate(AddressBookBase):
    pass


class Address(AddressBookBase):
    id: int
    
    class Config:
        orm_mode = True