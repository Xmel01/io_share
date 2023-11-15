from websockets.client import connect
import asyncio, pickle

async def hello():
    async with connect("ws://localhost:8765") as websocket:
        while True:
            try:
                message = await websocket.recv()
                print(f"Received: {pickle.loads(message)}")
            except Exception as e:
                print(e)

asyncio.run(hello())
