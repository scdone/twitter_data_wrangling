import asyncio

async def practice():
    print('ready...')
    await asyncio.sleep(2)
    print('set...')
    await asyncio.sleep(2)
    print('go!')

asyncio.run(practice())