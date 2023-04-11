def cart(set1, set2):
    cart = set()
    for item1 in set1:
        for item2 in set2:
            cart.add((item1, item2))
    return cart


# використання функції
set1 = {1, 2, 3}
set2 = {'a', 'b'}
result = cart(set1, set2)
print(result)
