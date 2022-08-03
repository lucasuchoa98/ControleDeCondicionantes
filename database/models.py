from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    favorites = relationship('Favorite', backref='user', lazy='subquery')


class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))


class Customer(Base):
    __tablename__ = 'custumer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    licence = relationship('Licence', backref='custumer', lazy='subquery')

class Licence(Base):
    __tablename__ = 'licence'
    licence_number =Column(Integer, primary_key=True)
    agency = Column(String)
    published_date = Column(Date)
    maturity = Column(Date)