def trans_complex_dict(weather):
    # Ініціалізація пустих звичайних словників
    weath1 = {}
    weath2 = {}
    weath3 = {}

    # Перетворюємо комплексного на окремі звичайні словники
    for key, value in weath.items():
        if key == 1:
            weath1 = value
        elif key == 2:
            weath2 = value
        elif key == 3:
            weath3 = value

    return weath1, weath2, weath3


# використання функції зі зазначеним словником
weath = {
    1: {"obsv": "sun", "tmpr": "hotly", "hmdt": "high", "wind": "no"},
    2: {"obsv": "sun", "tmpr": "hotly", "hmdt": "high", "wind": "there is"},
    3: {"obsv": "overcast", "tmpr": "hotly", "hmdt": "high", "wind": "no"}
}

weath1, weath2, weath3 = trans_complex_dict(weath)

# Виведення результатів
print("weather1:", weath1)
print("weather2:", weath2)
print("weather3:", weath3)
