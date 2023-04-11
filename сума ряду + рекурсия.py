def factor(n):
    if n == 0:
        return 1
    else:
        return n * factor(n-1)

def sum_series(n):
    if n == 0:
        return 0
    else:
        return (3 ** n) * (factor(n) // (n ** n)) + sum_series(n-1)

# значення n
n = int(input("Введіть значення N: "))

# Виклик функції для обчислення суми ряду
result = sum_series(n)

# Виведення результату
print("Сума ряду до", n, "дорівнює:", result)