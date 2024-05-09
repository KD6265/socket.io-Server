# chmod +x app/main.py
import sys
from pathlib import Path
import logging

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))
# from ..models import User
BASE_DIR = Path(__file__).resolve().parent.parent
print("Base directory:", BASE_DIR)


import psycopg2
import socketio
from fastapi import FastAPI
import uvicorn


from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import update


from dotenv import  load_dotenv
import os 
from init_db import demotb
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession

sio_server = socketio.AsyncServer(cors_allowed_origins=[], async_mode="asgi")

sio_app = socketio.ASGIApp(sio_server, socketio_path='sockets')
load_dotenv()

database_url = os.getenv("DATABASE_URL")
print("url :",database_url)
engine = create_async_engine(database_url)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

app = FastAPI()
app.mount("/", sio_app)

# Database update function
async def update_database():
    print("database call")
    try:
        async with async_session() as session:
            stmt = update(demotb).values(
                top=demotb.top * 2,
                bottom=demotb.bottom - 6,
                left=demotb.left + 2,
                right=demotb.right - 57
            )
            await session.execute(stmt)
            await session.commit()
            await session.close()
        print("database updated" )
    except psycopg2.Error as e:
        logging.error(f'An error occurred in database update : {e}')
        logging.error(f'Error updating database : {e}')
        print(f"Error updating database: {e}")

@sio_server.event
async def start_program(sid):
    await sio_server.emit('message', {'message': 'Program is started'}, room=sid)
    try:
        print(f"client id: {sid}")
        await update_database()
        await sio_server.emit('message', {'message': 'Program is completed'}, room=sid)
    except Exception as e:
        logging.error(f'An error occurred in database call : {e}')
        print(f"Error starting program: {e}")
def main():
    try:
        print("Starting server...")
        uvicorn.run('main:app', host="44.225.181.72", port=8000, reload=True)
    except Exception as e:
        logging.error(f'An error occurred in server start : {e}')
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    import asyncio
    # uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
    main()