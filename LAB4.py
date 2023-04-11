# Відношення R1
R1 = [("Іванов", "Математика", 5),
      ("Петренко", "Фізика", 3)]

# Відношення R2
R2 = [("Іванов", "Математика", 5),
      ("Іванов", "Фізика", 4)]

# Функція для виконання операції об'єднання
def union(R1, R2):
    return list(set(R1) | set(R2))

# виконання операції перетину
def inter(R1, R2):
    return list(set(R1) & set(R2))

# виконання операції різниці
def diff(R1, R2):
    return list(set(R1) - set(R2))

# Виконання операцій об'єднання, перетину та різниці
union_result = union(R1, R2)
inter_result = inter(R1, R2)
diff_result = diff(R1, R2)

# Виведення результатів
print("Результат об'єднання: ", union_result)
print("Результат перетину: ", inter_result)
print("Результат різниці: ", diff_result)