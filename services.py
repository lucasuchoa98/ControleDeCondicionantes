from datetime import date, timedelta
#from aiohttp import ClientSession
from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete

from database.models import Customer, Licence, User, Favorite
from database.connection import async_session

class CustomerService:
    async def create_customer(name:str):
        async with async_session() as session:
            session.add(Customer(name=name))
            await session.commit()

    async def delete_customer(custumer_id: int):
        async with async_session() as session:
            await session.execute(delete(Customer).where(Customer.id==custumer_id))
            await session.commit()

    async def list_user():
        async with async_session() as session:
            result = await session.execute(select(Customer))
            return result.scalars().all()
    
    async def get_by_id(customer_id):
        async with async_session() as session:
            result = await session.execute(select(Customer).where(Customer.id==Customer))
            return result.scalar()

class LicenceService:
    async def add_licence(customer_id: int, licence_number: str, agency:str, published_date: date, maturity:date):
        async with async_session() as session:
            session.add(Licence(customer_id=customer_id, licence_number= licence_number, agency = agency, published_date = published_date, maturity= maturity))
            await session.commit()

    async def remove_licence(customer_id: int, licence_number: str):
        async with async_session() as session:
            await session.execute(delete(Licence).where(Licence.customer_id==customer_id, Licence.licence_number==licence_number))
            await session.commit()


class UserService:
    async def create_user(name: str):
        async with async_session() as session:
            session.add(User(name=name))
            await session.commit()

    async def delete_user(user_id: int):
        async with async_session() as session:
            await session.execute(delete(User).where(User.id==user_id))
            await session.commit()

    async def list_user():
        async with async_session() as session:
            result = await session.execute(select(User))
            return result.scalars().all()
    
    async def get_by_id(user_id):
        async with async_session() as session:
            result = await session.execute(select(User).where(User.id==user_id))
            return result.scalar()

class FavoriteService:
    async def add_favorite(user_id: int, symbol: str):
        async with async_session() as session:
            session.add(Favorite(user_id=user_id, symbol=symbol))
            await session.commit()

    async def remove_favorite(user_id: int, symbol: str):
        async with async_session() as session:
            await session.execute(delete(Favorite).where(Favorite.user_id==user_id, Favorite.symbol==symbol))
            await session.commit()


'''
class AssetService:
    async def day_summary(symbol: str):
        async with ClientSession() as session:
            yesterday = date.today() - timedelta(days=1)
            url = f'https://www.mercadobitcoin.net/api/{symbol}/day-summary/{yesterday.year}/{yesterday.month}/{yesterday.day}/'
            response = await session.get(url)
            data = await response.json()
            return {
                'highest': data['highest'],
                'lowest': data['lowest'],
                'symbol': symbol
            }
'''