from operations import get_number_input, perform_operation 

def calculator():
    supported_ops = ['+', '-', '*', '/']
    print("--- Калькулятор (Модульна версія) ---")
    print("Для завершення введіть: exit")

    while True:
        op = input(f"\nОберіть операцію ({', '.join(supported_ops)}) або 'exit': ").lower()

        if op == "exit":
            print("Програма завершена.")
            break

        if op not in supported_ops:
            print("Помилка! Невідома операція. Спробуйте ще раз.")
            continue

        a = get_number_input("Введіть перше число: ")
        b = get_number_input("Введіть друге число: ")

        result = perform_operation(op, a, b)
        
        print("Результат:", result)

if __name__ == "__main__":
    calculator()