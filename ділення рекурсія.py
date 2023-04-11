def divid(a, b):
    if a < b:
        return 0
    else:
        return 1 + divid(a - b, b)

# Введення чисел, які потрібно поділити
a = int(input("Введіть ділене: "))
b = int(input("Введіть дільник: "))

# Виклик функції для цілочисельного ділення
result = divid(a, b)

# Виведення результату
print("Результат ділення:", result)
