from websockets.client import connect
import asyncio, pickle, pyautogui

x = 0
y = 0
async def hello():
    async with connect("ws://89.248.206.92:8765") as websocket:
        while True:
            new_x, new_y = pyautogui.position()
            if new_x != x or new_y != y:
                x, y = new_x, new_y
                await websocket.send(pickle.dumps([x, y]))
            await asyncio.sleep(0.1)

asyncio.run(hello())