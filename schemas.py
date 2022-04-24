from sqlite3 import Date
from typing import List, Optional
from datetime import date
from pydantic import BaseModel


class ClientBase(BaseModel):
    cnpj: str
    name: str
    address: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True    


class LicenseBase(BaseModel):
    licence_number: str
    start_date: date
    expiration_date: date
    detail: str
    agency: str

class LicenseCreate(LicenseBase):
    pass

class License(LicenseBase):
    id: int

    class Config:
        orm_mode = True    


