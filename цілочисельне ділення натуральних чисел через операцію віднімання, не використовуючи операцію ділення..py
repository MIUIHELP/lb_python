def divide(divid, divis):
    quotient = 0
    while divid >= divis:
        divid -= divis
        quotient += 1
    return quotient

# чиселa, які потрібно поділити
divid = int(input("Введіть ділене: "))
divis = int(input("Введіть дільник: "))

#divide для цілочисельного ділення
quotient = divide(divid, divis)

# Виведення результату ділення
print("Ділення", divid, "на", divis, "= ", quotient)

