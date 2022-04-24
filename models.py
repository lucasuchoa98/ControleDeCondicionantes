from http import client
from sqlite3 import Date
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

from datetime import date

class Client(Base):
    __tablename__="client"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String, index=True)
    name = Column(String, index=True)
    address = Column(String)

    license = relationship("Licence", back_populates="client")

class Licence(Base):
    __tablename__ = "licence"

    id = Column(Integer, primary_key=True, index=True)
    licence_number = Column(String, unique=True, index=True)
    start_date = Column(String)
    expiration_date = Column(Boolean, default=lambda: datetime.date)
    detail = Column(String)
    agency = Column(String)

    client_id = Column(Integer, ForeignKey("client.id"))

    #conditioning = relationship("Conditionings", back_populates="licence")
    client = relationship("Client", back_populates="license")

"""class Conditionings(Base):
    __tablename__ = "Conditionings"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    delivery_date = Column(Date)

    licence = relationship("Licence", back_populates="conditioning")
"""