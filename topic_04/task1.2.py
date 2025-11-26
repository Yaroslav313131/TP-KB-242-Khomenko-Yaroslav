def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Помилка! Ділення на нуль неможливе."
def get_number_input(prompt):
    #Запитує число від користувача, обробляючи виняток ValueError
    while True:
        try:
            user_input = input(prompt)
            return float(user_input)
        except ValueError:
            print("Помилка! Будь ласка, введіть коректне числове значення.")

print("--- Калькулятор ---")
print("Для завершення введіть: exit")

while True:
    op = input("\nОберіть операцію: +, -, *, /: ")

    if op == "exit":
        print("Програма завершена.")
        break  
    if op not in ('+', '-', '*', '/'):
        print("Помилка! Невідома операція. Спробуйте ще раз.")

    a = get_number_input("Введіть перше число: ")
    b = get_number_input("Введіть друге число: ")

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)

    print("Результат:", result)