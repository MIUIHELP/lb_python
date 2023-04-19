def find_multiples_of_three(lst):
    multiples = []  # Створюємо пустий список для зберігання знайдених елементів

    for item in lst:  # Перебираємо кожен елемент у списку
        if item % 3 == 0:  # Перевіряємо, чи є елемент кратним 3
            multiples.append(item)  # Якщо так, додаємо його до списку знайдених елементів

    multiples.sort()  # Сортуємо список знайдених елементів за зростанням

    return multiples  # Повертаємо список знайдених елементів


my_list = [1, 3, 5, 6, 9, 12, 15, 18, 21, 24]
result = find_multiples_of_three(my_list)
print(result)
