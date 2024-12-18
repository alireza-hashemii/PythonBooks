from multiprocessing import Pool
import time
import multiprocessing

print(multiprocessing.cpu_count())

def hello(name:str):
    return f'Hello World and to you {name}'

if __name__ == '__main__':
    with Pool() as process_pool:
        start = time.time()
        process_hello_one = process_pool.apply(hello, args=("Jack",))
        process_hello_two = process_pool.apply(hello, args=("Mandana",))
        end = time.time()

    print(process_hello_one)
    print(process_hello_two)
    print(f"All processes finished running in {end-start} second(s)")