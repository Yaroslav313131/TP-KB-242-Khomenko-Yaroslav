def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Ділення на нуль неможливе!"


op = input("Оберіть операцію: +, -, *, /: ")
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

if op == "+":
    print("Результат:", add(a, b))
elif op == "-":
    print("Результат:", sub(a, b))
elif op == "*":
    print("Результат:", mul(a, b))
elif op == "/":
    print("Результат:", div(a, b))
else:
    print("Помилка! Невідома операція.")