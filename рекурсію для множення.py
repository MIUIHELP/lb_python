def multi(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + multi(a, b - 1)
    else:
        return -multi(a, -b)

# Введення чисел, які потрібно перемножити
a = int(input("Введіть число №1: "))
b = int(input("Введіть число №2: "))

# Виклик функції для множення чисел
result = multi (a, b)

# Виведення результату
print("Результат множення:", result)
