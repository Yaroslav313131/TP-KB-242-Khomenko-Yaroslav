def discr(a, b, c):
    return b * b - 4 * a * c


a = int(input("What's A: "))
b = int(input("What's B: "))
c = int(input("What's C: "))

D = discr(a, b, c)

print (D)