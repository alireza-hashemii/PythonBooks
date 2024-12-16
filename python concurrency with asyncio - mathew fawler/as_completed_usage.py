# asynio.as_completed() is another asynchoronous functions witch 
# returns a list of futures that must be awaited. the only difference
# is that if a task finishes sooner than the others retrieving and
# having the answer earlier is possible. while other tasks are 
# proccesing you can have the answers of the ones got proccesed earlier.

import asyncio
import aiohttp
from aiohttp import ClientSession
import time

async def google_request(session:ClientSession, url:str, delay:int):
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [google_request(session,"https://www.google.com",5),
                 google_request(session,"https://www.google.com",3),
                 google_request(session,"https://www.google.com",1)]

        for i in asyncio.as_completed(tasks):
            result = await(i)
            print(result)
      

asyncio.run(main())