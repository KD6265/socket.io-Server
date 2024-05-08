import asyncio
import socketio

sio_client = socketio.AsyncClient()

@sio_client.event
async def connect():
    print('I\'m connected')
    await sio_client.emit('start_program',)  # Emit the start_program event
    # await sio_client.connect()

@sio_client.event
async def disconnect():
    print('I\'m disconnected')
    
async def start_program():
    await asyncio.sleep(5000)
    await sio_client.emit('start_program',)

@sio_client.event
async def message(data: dict):
    # print(f"client id: {sid}")
    message = data.get('message')
    print(f"{message}")

async def main():
    await sio_client.connect(url='http://127.0.0.1:8000', socketio_path='sockets')
    await asyncio.sleep(1)  # add this line to give the connection time to establish
    await sio_client.disconnect()
if __name__ == '__main__':
    asyncio.run(main()) 
# asyncio.run(main())