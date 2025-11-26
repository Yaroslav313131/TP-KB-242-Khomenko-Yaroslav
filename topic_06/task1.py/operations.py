from functions import add, sub, mul, div 

def get_number_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            return float(user_input)
        except ValueError:
            print("Помилка! Будь ласка, введіть коректне числове значення.")

def perform_operation(op, a, b):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    elif op == "*":
        return mul(a, b)
    elif op == "/":
        return div(a, b)
    else:
        return "Помилка! Невідома операція."