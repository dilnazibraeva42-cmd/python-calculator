# Simple console calculator
from src.advanced import power, percent
from src.validation import get_number


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


OPERATIONS = {
    "1": add,
    "2": subtract,
    "3": multiply,
    "4": divide,
    "5": power,
    "6": percent,
}

MENU = """
=== Python Calculator ===
1. Сложение
2. Вычитание
3. Умножение
4. Деление
5. Возведение в степень
6. Процент от числа
0. Выход
"""


def main():
    print("Python Calculator: консольный калькулятор")
    while True:
        print(MENU)
        choice = input("Выберите действие (0-6): ")
        if choice == "0":
            print("До свидания!")
            break
        if choice not in OPERATIONS:
            print("Неверный выбор")
            continue
        a = get_number("Первое число: ")
        b = get_number("Второе число: ")
        print("Результат:", OPERATIONS[choice](a, b))


if __name__ == "__main__":
    main()
