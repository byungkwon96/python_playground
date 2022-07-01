from threading import Thread, Lock
from queue import Queue
import time

# global variable
database_value = 0
# or u can use ---> with lock:


def increase(Lock):
    global database_value
    # lock prevents other threads to access the variable
    lock.acquire()
    local_copy = database_value

    # processing
    local_copy += 1

    # other threads runs when one thread is sleeping
    time.sleep(0.1)
    database_value = local_copy
    # lock needs to get released or it will stop forever here
    lock.release()


if __name__ == "__main__":
    lock = Lock()
    print("start value ", database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End Value ", database_value)

    print("End multi treading")

    # first in first out data strucutre
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)

    first = q.get()
    second = q.get()

    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=increase, args=(lock,))
        # back groudn thread that dies when main dies
        thread.daemon = True
        thread.start()
