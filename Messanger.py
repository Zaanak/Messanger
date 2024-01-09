import asyncio
from datetime import datetime

async def handle_client(reader, writer):
    writer.write( bytes(str(datetime.now())+'\n', 'utf-8') )
    await writer.drain()

    for i in range(10):
        received = await reader.readline()
        writer.write(received + b'\n')
        await writer.drain()

    writer.close()
    await writer.wait_closed()


if __name__ == "__main__":
    host = 'localhost'
    port = 6767

    event_loop = asyncio.get_event_loop()
    server_task = asyncio.start_server(handle_client, host=host, port=port)

    event_loop.run_until_complete(server_task)
    event_loop.run_forever()