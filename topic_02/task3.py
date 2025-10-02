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

match op:
    case "+":
        print("Результат:", add(a, b))
    case "-":
        print("Результат:", sub(a, b))
    case "*":
        print("Результат:", mul(a, b))
    case "/":
        print("Результат:", div(a, b))
    case _:
        print("Помилка! Невідома операція.")