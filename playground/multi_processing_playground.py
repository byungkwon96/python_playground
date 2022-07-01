from multiprocessing import Process, Value, Array, Lock, Pool
from threading import Thread
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


processes = []
num_process = os.cpu_count()

# create processs
for i in range(num_process):
    p = Process(target=square_numbers)
    processes.append(p)

# start
for p in processes:
    p.start()

# join
for p in processes:
    p.join()

print("end main")


# one process = one cpu but multiple threads
threads = []
num_threads = 10

# create thread
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# start
for t in threads:
    t.start()

# join
for t in threads:
    t.join()

print("end threads")


def add_100(number, lock):
    with lock:
        for i in range(100):
            time.sleep(0.01)
            number.value += 1


def cube(number):
    return number * number * number


# since processing cannot share data we use Value() and Array()
if __name__ == "__main__":

    lock = Lock()
    shared_number = Value("i", 0)
    print("Number at beginning is ", shared_number.value)

    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Number at end is ", shared_number.value)

    # process pool manange the pool
    pool = Pool()
    numbers = range(10)
    # map,apply, join,close
    result = pool.map(cube, numbers)  # allocate maximum number of process

    pool.close()
    pool.join()

    print(result)