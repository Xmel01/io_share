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

import asyncio
from websockets.server import serve

gru = None
minion = None
async def echo(websocket):
    global gru, minion
    if gru is None:
        gru = websocket
        gru.send("Connected")
    else:
        minion = websocket
        minion.send("Connected")

    if gru and minion:
        while True:
            for message in websocket:
                await minion.send(message)
                await asyncio.sleep(0.1)
    else:
        gru.send("await for peers")
        minion.send("await for peers")

async def main():
    async with serve(echo, "89.248.206.92", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())




