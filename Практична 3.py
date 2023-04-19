def count_words(sntnc):
    word = sntnc.split()
    return len(word)


def count_sentences(sntnc):
    sentences = sntnc.split('.')
    return len(sentences)


def count_unique_words(sntnc):
    word = sntnc.split()
    unique_words = set(word)
    return len(unique_words)


def count_unique_and_repeating_words(sntnc):
    words = sntnc.split()
    unique_words = set(words)
    repeating_words = []
    for word in unique_words:
        if words.count(word) > 1:
            repeating_words.append(word)
    return len(unique_words), repeating_words


def count_special_characters(sntnc):
    special_chars = [' ', '.', ',', '?', '!']
    special_char_count = {}
    for char in special_chars:
        special_char_count[char] = sntnc.count(char)
    return special_char_count


def find_numbers(sntnc):
    words = sntnc.split()
    numbers = []
    for word in words:
        if word.isdigit():
            numbers.append(int(word))

    return numbers


# Зчитуємо вхідний рядок від користувача
input_string = input("Введіть рядок тексту: ")

# Викликаємо функції для виконання різних завдань
word_count = count_words(input_string)
sentence_count = count_sentences(input_string)
unique_word_count = count_unique_words(input_string)
unique_words, repeating_words = count_unique_and_repeating_words(input_string)
special_char_count = count_special_characters(input_string)
numbers = find_numbers(input_string)

# Виводимо результати на екран
print("Кількість слів у рядку: ", word_count)
print("Кількість речень у рядку: ", sentence_count)
print("Кількість неповторюваних слів у рядку: ", unique_word_count)
print("Кількість унікальних слів у рядку: ", unique_words)
print("Кількість унікальних та повторюваних слів у рядку: ", repeating_words)
print("Частота використання слів, які зустрічаються більше, ніж два рази: ")
for word in repeating_words:
    print(word, ": ", input_string.count(word))
print("Кількість розділових знаків у рядку: ")
for char, count in special_char_count.items():
    print(char, ": ", count)
print("Кількість чисел у рядку: ", len(numbers))
print("Числа, знайдені у рядку: ", numbers)
