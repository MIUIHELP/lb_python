# Оголошення матриці
matrix = [
    [1, 4, 7],
    [21, 19, 5],
    [6, 11, 9]
]

# Створення списку з елементів матриці
elements_list = []
for row in matrix:
    for element in row:
        elements_list.append(element)

# середнє арифметичного всіх елементів
sum_all_elements = sum(elements_list)
average = sum_all_elements / len(elements_list)

# сума непарних елементів
sum_odd_elements = sum([element for element in elements_list if element % 2 != 0])

# добутку елементів головної діагоналі
diagonal_product = 1
for i in range(len(matrix)):
    diagonal_product *= matrix[i][i]

# Виведення результатів
print("Середнє арифметичне всіх елементів: ", average)
print("Сума непарних елементів: ", sum_odd_elements)
print("Добуток елементів головної діагоналі: ", diagonal_product)
