def find_nsk(a, b):
    # Знаходимо найбільший спільний дільник
    def find_gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    # Використовуємо формулу НСК = |a * b| / НСД(a, b)
    gcd = find_gcd(a, b)
    lcm = abs(a * b) // gcd
    return lcm

# Введення двох цілих чисел від користувача
num1 = int(input("Введіть перше ціле число: "))
num2 = int(input("Введіть друге ціле число: "))

# Виклик функції find_lcm та виведення результату
result = find_nsk(num1, num2)
print("Найменше спільне кратне:", result)
