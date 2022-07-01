from multiprocessing import Process
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
