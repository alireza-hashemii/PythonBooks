from concurrent.futures import ProcessPoolExecutor
import asyncio
from asyncio import AbstractEventLoop
from functools import partial


def count(to_number:int):
    counter = 0
    print(f"counting starts from 0 to number {to_number}")
    while counter < to_number:
        counter += 1

    return counter

async def main():
    with ProcessPoolExecutor() as process_pool_ex:
        event_loop: AbstractEventLoop = asyncio.get_running_loop()
        numbers = [3,6,12,100000000]
        calls = [partial(count, number) for number in numbers]
        call_coros = []

        for call in calls:
            call_coros.append(event_loop.run_in_executor(process_pool_ex,call))
        
        results = await asyncio.gather(*call_coros)
        for result in results:
            print(result)

if __name__ == "__main__":
 asyncio.run(main())