choose = int(input("Введите высоту треугольника "))

def traingol():
    a = choose
    b = -2
    print(' ' * choose, "**")
    for i in range(choose):
        a = a - 1
        b = b + 2
        print(" " * a, "*", " " * b, "*")
    print("*" * (choose * 2 + 2))


traingol()