from multiprocessing import Process
import time

def count(to_number:int):
    start = time.time()
    counter = 0
    while counter < to_number:
        counter += 1
    end = time.time()
    print(f'Looping Happened from 0 to {to_number} in {end-start} second(s)')
    return counter

if __name__ == '__main__':
    count_to_hundred_million = Process(target=count, args=(100000000,))
    count_to_twohundred_milloin = Process(target=count, args=(200000000,))

    start = time.time()
    count_to_hundred_million.start()
    count_to_twohundred_milloin.start()

    count_to_twohundred_milloin.join()
    count_to_hundred_million.join()
    end = time.time()
    print(f"All processes finished running in {end-start} second(s)")