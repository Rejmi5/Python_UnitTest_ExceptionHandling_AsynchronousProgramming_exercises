#-------------------------------------------------------------------------------
#Python Exception Handling - zadania

#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
"""
# Obsługuje wyjątek dzielenia przez zero
try:
    # Próba dzielenia 1 przez 0
    result = 1 / 0
except ZeroDivisionError:
    print("Nie można dzielić przez zero.")
"""

#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
"""
# Prosi o wprowadzenie liczby całkowitej i obsługuje ValueError
try:
    user_input = input("Wprowadź liczbę całkowitą: ")
    if not user_input.isdigit():
        raise ValueError("To nie jest liczba całkowita.")
except ValueError as e:
    print(e)
"""

#3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
"""
# Obsługuje wyjątek, gdy plik nie istnieje
try:
    # Próba otwarcia nieistniejącego pliku
    with open("nieistniejacy_plik.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Plik nie został znaleziony.")
"""

#4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
"""
# Prosi o wprowadzenie dwóch liczb i obsługuje TypeError
try:
    number1 = input("Wprowadź pierwszą liczbę: ")
    number2 = input("Wprowadź drugą liczbę: ")
    if not number1.replace('.', '', 1).isdigit() or not number2.replace('.', '', 1).isdigit():
        raise TypeError("Wprowadzone wartości muszą być liczbowe.")
    result = float(number1) + float(number2)
    print("Wynik dodawania to:", result)
except TypeError as e:
    print(e)
"""

#5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
"""
# Obsługuje wyjątek, gdy nie ma uprawnień do pliku
try:
    # Próba zapisu do pliku, do którego nie ma się uprawnień
    with open("/system_file.txt", "w") as file:
        file.write("Test")
except PermissionError:
    print("Nie masz uprawnień do zapisu w tym pliku.")
"""

#6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
"""
# Obsługuje wyjątek, gdy indeks jest poza zakresem listy
try:
    # Lista z trzema elementami
    my_list = [1, 2, 3]
    # Próba dostępu do elementu o indeksie 10
    print(my_list[10])
except IndexError:
    print("Indeks poza zakresem.")
"""

#7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
"""
# Obsługuje wyjątek, gdy użytkownik anuluje wprowadzenie danych
try:
    number = input("Wprowadź liczbę: ")
    print("Wprowadzona liczba to:", number)
except KeyboardInterrupt:
    print("\nWprowadzanie danych zostało przerwane przez użytkownika.")
"""

#8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
"""
# Obsługuje wyjątek arytmetyczny podczas dzielenia
try:
    # Próba dzielenia przez zero
    result = 10 / 0
except ArithmeticError:
    print("Wystąpił błąd arytmetyczny.")
"""

#9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
"""
# Obsługuje wyjątek, gdy występuje problem z kodowaniem pliku
try:
    # Próba odczytu pliku w niewłaściwym kodowaniu
    with open("plik.txt", "r", encoding="ascii") as file:
        content = file.read()
except UnicodeDecodeError:
    print("Problem z dekodowaniem pliku.")
"""

#10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
"""
# Obsługuje wyjątek, gdy atrybut nie istnieje
try:
    # Lista z elementami
    my_list = [1, 2, 3]
    # Próba wywołania nieistniejącej metody
    my_list.sortme()
except AttributeError:
    print("Wybrany atrybut nie istnieje.")
"""