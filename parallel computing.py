import threading
import time

def f_1 (start, end):
    total_1 = 0
    for x in range (start, end):
        total_1 += x**2 - x**2 + x**4 - x**5 + x + x
    return total_1

def f_2 (start, end):
    total_2 = 0
    for x in range (start, end):
        total_2 += x + x
    return total_2

start_1 = time.time
thread_1 = threading.Thread (target=f_1)

start_2 = time.time
thread_2 = threading.Thread (target=f_2)

thread_1.start()
thread_2.start()

if thread_1.is_alive() == 0:
    dur_1 = time.time - start_1
if thread_2.is_alive() == 0:
    dur_2 = time.time - start_2

thread_1.join()
thread_2.join()

total = total_1 + total_2

