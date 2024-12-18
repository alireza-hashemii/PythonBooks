from multiprocessing import Process
import time
from concurrent.futures import ProcessPoolExecutor


def count(to_number:int):
    start = time.time()
    counter = 0
    while counter < to_number:
        counter += 1
    end = time.time()
    print(f'Looping Happened from 0 to {to_number} in {end-start} second(s)')
    return counter

if __name__ == '__main__':
    numbers = [100000000,10,14,18,100000000]
    with ProcessPoolExecutor() as process_pool_exc:
        for result in process_pool_exc.map(count, numbers):
            print(result)
    