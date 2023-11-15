# import pyperclip
# import time
#
# def watch_clipboard():
#     last_clipboard = None
#     while True:
#         current_clipboard = pyperclip.paste()
#         if current_clipboard != last_clipboard:
#             print("Буфер обмена изменен:", current_clipboard)
#             last_clipboard = current_clipboard
#         time.sleep(1)  # Задержка 1 секунда
#
# if __name__ == "__main__":
#     watch_clipboard()

import pyautogui, asyncio, pickle
from websockets.server import serve
x = 0
y = 0
connected = set()
async def echo(websocket):
    global x, y
    while True:
        new_x, new_y = pyautogui.position()
        if new_x != x or new_y != y:
            x, y = new_x, new_y
            await websocket.send(pickle.dumps([x, y]))
        await asyncio.sleep(0.1)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())




