def multi(a, b):
    result = 0
    for i in range(b):
        result += a
    return result

# Введення чисел, які потрібно помножити
a = int(input("Введіть число №1: "))
b = int(input("Введіть число №2: "))

# Виклик функції
sum = multi(a, b)

# Виведення результату
print("Добуток чисел", a, "та", b, "дорівнює:", sum)