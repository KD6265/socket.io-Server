import psycopg2
import socketio
from fastapi import FastAPI
import uvicorn

# for sqlalchemy
from sqlalchemy import create_engine,text
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

# for sqlalchemy-aiohttp
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
    
# Initialize Socket.IO server
sio_server = socketio.AsyncServer(cors_allowed_origins=[], async_mode="asgi")

sio_app = socketio.ASGIApp(sio_server, socketio_path='sockets')

#database connection
engine = create_async_engine(URL.create(
    drivername="postgresql+asyncpg",username="postgres",password="Kd1606",host="localhost",port="7000",database="demodb"
) )
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

app = FastAPI()
app.mount("/", sio_app)

# Database update function
async def update_database():
    print("database call")
    try:
        
        async with async_session() as session:
            await session.execute(text("""
            UPDATE demotb
            SET
                "top" = "top"*2,
                "bottom" = "bottom"-6,
                "left" = "left"+2,
                "right" = "right"-57
        """))
            await session.commit()
            await session.close()
        print("database updated" )
        
    except psycopg2.Error as e:
        print(f"Error updating database: {e}")

@sio_server.event
async def start_program(sid):
    await sio_server.emit('message', {'message': 'Program is started'}, room=sid)
    try:
        print(f"client id: {sid}")
        await update_database()
        await sio_server.emit('message', {'message': 'Program is completed'}, room=sid)
    except Exception as e:
        print(f"Error starting program: {e}")

if __name__ == '__main__':
    print("Starting server...")
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
