from pydantic import BaseModel

class HotelIn(BaseModel):
    email: str
    password: str

class HotelOut(BaseModel):
    email: str
    ubication: str
    name: str
    price: int


class HotelAdd(BaseModel):
    email: str
    password: str
    ubication: str
    username: str
    price: int 