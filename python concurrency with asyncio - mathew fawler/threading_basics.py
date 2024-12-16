import threading 
import os

def hello_thread():
    thread_aanouncemnt = threading.current_thread()
    print(thread_aanouncemnt)

new_thread_hello = threading.Thread(target=hello_thread)
new_thread_hello.start()
print(threading.active_count())
new_thread_hello.join()
print(threading.current_thread())



# procces_id = os.getpid()
# number_of_threads = threading.active_count()
# current_thread_name = threading.current_thread().name


# print(procces_id)
# print(number_of_threads)
# print(current_thread_name)