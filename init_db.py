import os
import asyncio
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database
load_dotenv()

# Example: DATABASE_URL="postgresql+asyncpg://username:password@localhost:5432/database_name"
DATABASE_URL = os.getenv("DATABASE_URL")
print('Database url : ', DATABASE_URL)

#create db  
# async def create_db():
#     if await database_exists(DATABASE_URL):
#         print("Database exists!")
#     else:
#         print("Database does not exist.")
#         await create_database(DATABASE_URL) 
# async def create_db():
#     async_engine = create_async_engine(DATABASE_URL, echo=True, future=True)
#     async with async_engine.connect() as conn:
#         if not await conn.run_sync(database_exists(async_engine.url)):
#             await conn.run_sync( create_database(DATABASE_URL))
#             print('database created')
#         else:
#             print('database already exists')
async_engine = create_async_engine(DATABASE_URL, echo=True, future=True)

Base = declarative_base()

class demotb(Base):
    __tablename__ = 'demotb'

    id = Column(Integer, primary_key=True)
    top = Column(Integer)
    bottom = Column(Integer)
    left = Column(Integer)
    right = Column(Integer)
async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    # await create_db()
    await create_tables()


asyncio.run(main())

SessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)
# Create a session
async def get_session():
    async with SessionLocal() as session:
        yield session

print("Tables created successfully")
