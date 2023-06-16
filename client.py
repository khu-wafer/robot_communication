import asyncio
import websockets

async def send_message():
    async with websockets.connect('ws://{YOUR_IP}:8080') as websocket:
        while True:
            message = input("Enter a message (or 'exit' to quit): ")
            await websocket.send(message)
            if message == 'exit':
                break
            response = await websocket.recv()
            print(f"Received response: {response}")

asyncio.get_event_loop().run_until_complete(send_message())
