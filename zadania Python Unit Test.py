#-------------------------------------------------------------------------------
#Python Unit test - zadania

#1. Write a Python unit test program to check if a given number is prime or not.
"""
import unittest

def is_prime(number):
    # Sprawdza czy liczba jest liczbą pierwszą
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

class TestPrimeNumber(unittest.TestCase):
    # Klasa testowa dla funkcji is_prime

    def test_prime(self):
        # Test sprawdzający czy liczba jest pierwsza
        self.assertTrue(is_prime(5))  # 5 jest liczbą pierwszą

    def test_not_prime(self):
        # Test sprawdzający czy liczba nie jest pierwsza
        self.assertFalse(is_prime(4))  # 4 nie jest liczbą pierwszą

if __name__ == "__main__":
    unittest.main()
"""

#2. Write a Python unit test program to check if a list is sorted in ascending order.
"""
import unittest

def is_sorted(list):
    # Sprawdza czy lista jest posortowana rosnąco
    return all(list[i] <= list[i+1] for i in range(len(list) - 1))

class TestSorted(unittest.TestCase):
    # Klasa testowa dla funkcji is_sorted

    def test_sorted(self):
        # Test sprawdzający czy lista jest posortowana
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))  # Lista jest posortowana

    def test_not_sorted(self):
        # Test sprawdzający czy lista nie jest posortowana
        self.assertFalse(is_sorted([5, 4, 3, 2, 1]))  # Lista nie jest posortowana

if __name__ == "__main__":
    unittest.main()
"""

#3. Write a Python unit test program that checks if two lists are equal.
"""
import unittest

def are_lists_equal(list1, list2):
    # Sprawdza czy dwie listy są takie same
    return list1 == list2

class TestListEquality(unittest.TestCase):
    # Klasa testowa dla funkcji are_lists_equal

    def test_equal_lists(self):
        # Test sprawdzający czy listy są równe
        self.assertTrue(are_lists_equal([1, 2, 3], [1, 2, 3]))

    def test_not_equal_lists(self):
        # Test sprawdzający czy listy nie są równe
        self.assertFalse(are_lists_equal([1, 2, 3], [3, 2, 1]))

if __name__ == "__main__":
    unittest.main()
"""

#4. Write a Python unit test program to check if a string is a palindrome.
"""
import unittest

def is_palindrome(string):
    # Sprawdza czy łańcuch znaków jest palindromem
    return string == string[::-1]

class TestPalindrome(unittest.TestCase):
    # Klasa testowa dla funkcji is_palindrome

    def test_palindrome(self):
        # Test sprawdzający czy łańcuch znaków jest palindromem
        self.assertTrue(is_palindrome("radar"))

    def test_not_palindrome(self):
        # Test sprawdzający czy łańcuch znaków nie jest palindromem
        self.assertFalse(is_palindrome("hello"))

if __name__ == "__main__":
    unittest.main()
"""

#5. Write a Python unit test program to check if a file exists in a specified directory.
"""
import unittest
import os

def file_exists(directory, filename):
    # Sprawdza czy plik istnieje w danym katalogu
    return os.path.exists(os.path.join(directory, filename))

class TestFileExistence(unittest.TestCase):
    # Klasa testowa dla funkcji file_exists

    def test_file_exists(self):
        # Test sprawdzający czy plik istnieje
        self.assertTrue(file_exists(".", "test_file.txt"))  # Załóżmy, że plik 'test_file.txt' istnieje w bieżącym katalogu

    def test_file_does_not_exist(self):
        # Test sprawdzający czy plik nie istnieje
        self.assertFalse(file_exists(".", "nonexistent_file.txt"))

if __name__ == "__main__":
    unittest.main()
"""

#6. Write a Python unit test that checks if a function handles floating-point calculations accurately.
"""
import unittest

def calculate_float(a, b):
    # Przeprowadza obliczenia na liczbach zmiennoprzecinkowych
    return a / b

class TestFloatCalculations(unittest.TestCase):
    # Klasa testowa dla funkcji calculate_float

    def test_float_calculation(self):
        # Test sprawdzający obliczenia na liczbach zmiennoprzecinkowych
        self.assertAlmostEqual(calculate_float(1.0, 3.0), 0.333333, places=6)

if __name__ == "__main__":
    unittest.main()
"""

#7. Write a Python unit test program to check if a function handles multi-threading correctly.
"""
import unittest
import threading

def increment_counter(counter):
    # Zwiększa licznik w kontekście wielowątkowym
    with threading.Lock():
        counter.value += 1

class Counter:
    # Klasa licznika zabezpieczona przed współbieżnym dostępem
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        # Bezpieczne inkrementowanie licznika
        with self._lock:
            self.value += 1

class TestMultiThreading(unittest.TestCase):
    # Klasa testowa dla operacji wielowątkowych

    def test_threading(self):
        # Test sprawdzający poprawność operacji wielowątkowych
        counter = Counter()
        threads = [threading.Thread(target=counter.increment) for _ in range(10)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual(counter.value, 10)

if __name__ == "__main__":
    unittest.main()
"""

#8. Write a Python unit test program to check if a database connection is successful.
"""
import unittest
import sqlite3

def connect_to_db(path):
    # Próbuje nawiązać połączenie z bazą danych
    connection = sqlite3.connect(path)
    return connection

class TestDatabaseConnection(unittest.TestCase):
    # Klasa testowa dla połączenia z bazą danych

    def test_connection(self):
        # Test sprawdzający czy połączenie z bazą danych jest możliwe
        conn = connect_to_db(':memory:')  # używamy bazy danych w pamięci
        self.assertIsInstance(conn, sqlite3.Connection)
        conn.close()

if __name__ == "__main__":
    unittest.main()
"""

#9. Write a Python unit test program to check if a database query returns the expected results.
"""
import unittest
import sqlite3

def query_db(connection, query):
    # Wykonuje zapytanie do bazy danych
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

class TestDatabaseQuery(unittest.TestCase):
    # Klasa testowa dla zapytań do bazy danych

    def test_query(self):
        # Test sprawdzający czy zapytanie do bazy danych zwraca oczekiwane wyniki
        conn = sqlite3.connect(':memory:')
        conn.execute('CREATE TABLE test (id INTEGER)')
        conn.execute('INSERT INTO test (id) VALUES (1), (2), (3)')
        result = query_db(conn, 'SELECT id FROM test')
        self.assertEqual(result, [(1,), (2,), (3,)])
        conn.close()

if __name__ == "__main__":
    unittest.main()
"""

#10. Write a Python unit test program to check if a function correctly parses and validates input data.
import unittest

def parse_input(data, datatype):
    # Analizuje i waliduje dane wejściowe zgodnie z oczekiwanym typem danych
    if not isinstance(data, datatype):
        raise ValueError("Nieprawidłowy typ danych")
    return data

class TestInputParsing(unittest.TestCase):
    # Klasa testowa dla analizy danych wejściowych

    def test_parse_valid(self):
        # Test sprawdzający poprawną analizę danych
        self.assertEqual(parse_input(123, int), 123)

    def test_parse_invalid(self):
        # Test sprawdzający reakcję na nieprawidłowe dane
        with self.assertRaises(ValueError):
            parse_input("123", int)

if __name__ == "__main__":
    unittest.main()
