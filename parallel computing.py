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

def f (iterations):
    
    start_time_1 = time.time()
    result_1 = f_1 (0, iterations)
    dur_1 = time.time() - start_time_1

    start_time_2 = time.time()
    result_2 = f_2 (0, iterations)
    dur_2 = time.time() - start_time_2

    start_time_3 = time.time()
    total = result_1 + result_2
    dur_3 = time.time() - start_time_3

    thread_1 = threading.Thread(target=f_1)
    thread_2 = threading.Thread(target=f_2)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()
    
    return dur_1, dur_2, dur_3, total

dur_10000 = f(10000)

dur_100000 = f(100000)

print(f"Длительность выполнения для 10 000 итераций:")
print(f" - Формула 1: {dur_10000[0]:.4f} секунд")
print(f" - Формула 2: {dur_10000[1]:.4f} секунд")
print(f" - Итоговое вычисление: {dur_10000[2]:.4f} секунд")
print(f" - Общий результат: {dur_10000[3]}")

print(f"\nДлительность выполнения для 100 000 итераций:")
print(f" - Формула 1: {dur_100000[0]:.4f} секунд")
print(f" - Формула 2: {dur_100000[1]:.4f} секунд")
print(f" - Итоговое вычисление: {dur_100000[2]:.4f} секунд")
print(f" - Общий результат: {dur_100000[3]}")