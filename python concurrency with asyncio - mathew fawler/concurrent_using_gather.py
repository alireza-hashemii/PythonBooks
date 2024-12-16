# what asyncio.gather() does? it enables us to make requests 
# asynchoronously and returns a list of raw values that can be looped
# through. we can have return_exceptions=True in order to handle 
# exceptions manualy(but remember in this it is expected to loop
# through the list of answers and count or pull out the exceptions.)
# The other drawback of gather is if one tasks encounter an exception
# there is no way to cancel others. and you have to wait for all of 
# coroutines to finish processing in order to retrieve the list
# of answers. 

import asyncio
import aiohttp
from aiohttp import ClientSession
import time

async def google_request(session:ClientSession, url:str):
    async with session.get(url) as result:
        return result.status

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [google_request(session,"https://www.google.com") for _ in range(90)]
        start = time.time()
        try:
            result = await asyncio.wait_for(asyncio.gather(*tasks),timeout=10)
            print(result)
        except asyncio.TimeoutError:
            print("Reached a Timeout") 
        end = time.time()

        print(end - start)
        
        
asyncio.run(main())