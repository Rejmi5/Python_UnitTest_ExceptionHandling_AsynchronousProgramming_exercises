#-------------------------------------------------------------------------------
#Python Asynchronous Programming - zadania

#1. Write a Python program that creates an asynchronous function to print "Python Exercises!" with a two second delay.
"""
import asyncio
import time

# Asynchroniczna funkcja z logowaniem
async def print_message_with_logging():
    start_time = time.time()
    await asyncio.sleep(2)
    print("Python Exercises!")
    print(f"Logged at {time.time() - start_time:.2f} seconds.")

async def main():
    await print_message_with_logging()

asyncio.run(main())
"""

#2. Write a Python program that creates three asynchronous functions and displays their respective names with different delays (1 second, 2 seconds, and 3 seconds).
"""
import asyncio

# Funkcje asynchroniczne z różnymi opóźnieniami i powiadomieniami
async def async_function(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} completed after {delay} seconds.")

async def run_functions():
    await asyncio.gather(
        async_function("Function 1", 1),
        async_function("Function 2", 2),
        async_function("Function 3", 3)
    )

asyncio.run(run_functions())
"""

#3. Write a Python program that creates an asyncio event loop and runs a coroutine that prints numbers from 1 to 7 with a delay of 1 second each.
"""
import asyncio

# Coroutine wyświetlająca liczby z dynamicznym opóźnieniem
async def print_numbers_with_delay():
    delay = 0.5
    for number in range(1, 8):
        await asyncio.sleep(delay)
        print(number)
        delay += 0.5  # Zwiększ opóźnienie o 0.5 sekundy za każdym razem

asyncio.run(print_numbers_with_delay())
"""

#4. Write a Python program that implements a coroutine to fetch data from two different URLs simultaneously using the "aiohttp" library.
"""
import asyncio
import aiohttp
import time

# Korutyna pobierająca dane z URL i rejestrująca czas
async def fetch_data(url):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            print(f"Data from {url} fetched in {time.time() - start_time:.2f} seconds.")
            return data

async def fetch_multiple_urls():
    urls = ["https://www.youtube.com", "https://www.facebook.com"]
    await asyncio.gather(*(fetch_data(url) for url in urls))

asyncio.run(fetch_multiple_urls())
"""

#5. Write a Python program that runs multiple asynchronous tasks concurrently using asyncio.gather() and measures the time taken.
"""
import asyncio
import time

# Asynchroniczne zadanie robocze
async def worker(task_number, delay):
    await asyncio.sleep(delay)
    print(f"Task {task_number} completed after {delay} seconds.")

# Funkcja uruchamiająca wszystkie zadania i mierząca czas ich wykonania
async def run_concurrent_tasks():
    start_time = time.time()
    tasks = [worker(i, i*0.5) for i in range(1, 6)]  # Przykładowe zadania z rosnącymi opóźnieniami
    await asyncio.gather(*tasks)
    total_time = time.time() - start_time
    print(f"All tasks completed in {total_time:.2f} seconds.")

asyncio.run(run_concurrent_tasks())
"""

#6. Write a Python program to create a coroutine that simulates a time-consuming task and use asyncio.CancelledError to handle task cancellation.
"""
import asyncio

# Długotrwała korutyna
async def long_running_task():
    try:
        await asyncio.sleep(10)  # Symuluje długie zadanie
        print("Task completed.")
    except asyncio.CancelledError:
        print("Task was cancelled!")

async def main():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(2)  # Anuluj zadanie po 2 sekundach
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Main noticed that the task was cancelled.")

asyncio.run(main())
"""

#7. Write a Python program that implements a timeout for an asynchronous operation using asyncio.wait_for().
"""
import asyncio

# Zadanie, które może przekroczyć limit czasu
async def possibly_long_task():
    await asyncio.sleep(5)  # Symuluje zadanie, które może trwać dłużej niż limit czasowy
    return "Task completed."

async def main():
    try:
        # Uruchom zadanie z limitem czasowym 3 sekundy
        result = await asyncio.wait_for(possibly_long_task(), timeout=3)
        print(result)
    except asyncio.TimeoutError:
        print("The task did not complete on time!")

asyncio.run(main())
"""

#8. Write a Python program that uses asyncio queues to simulate a producer-consumer scenario with multiple producers and a single consumer.
"""
import asyncio
import random

# Producent dodający elementy do kolejki
async def producer(queue, name):
    for _ in range(10):
        item = random.randint(1, 100)
        await queue.put(item)
        print(f"Producer {name} produced {item}")
        await asyncio.sleep(random.random())

# Konsument pobierający elementy z kolejki
async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumer consumed {item}")
        await asyncio.sleep(random.random())
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=10)
    producers = [asyncio.create_task(producer(queue, n)) for n in range(3)]
    consumers = [asyncio.create_task(consumer(queue)) for _ in range(1)]
    await asyncio.gather(*producers)
    await queue.join()  # Czekaj, aż wszystkie elementy zostaną przetworzone
    for c in consumers:
        c.cancel()  # Zakończ konsumentów

asyncio.run(main())
"""