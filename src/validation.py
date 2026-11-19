def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Ошибка: введите число")
