# prog2.py
value = input("Введите атомный номер элемента Z: ")
if value:
    Z = float(value)
    if Z == 3:
        print("Li")
    elif  Z == 25:
        print("Mn")
    elif  Z == 80:
        print ("Hg")
    elif Z == 17:
        print ("Cl")
    else:
        print("Я такого не знаю!")
else:
    print("Введите значение атомного номера элемента Z!")
