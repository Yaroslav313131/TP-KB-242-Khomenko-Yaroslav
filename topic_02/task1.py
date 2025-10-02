import math

def discr(a, b, c):
    return b * b - 4 * a * c

def solve_quadratic(a, b, c):
    D = discr(a, b, c)
    print("Дискримінант:", D)

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("Два різних корені: x1 =", x1, ", x2 =", x2)
    elif D == 0:
        x = -b / (2 * a)
        print("Один корінь: x =", x)
    else:
        print("Коренів немає (D < 0)")

a = int(input("What's A: "))
b = int(input("What's B: "))
c = int(input("What's C: "))

solve_quadratic(a, b, c)