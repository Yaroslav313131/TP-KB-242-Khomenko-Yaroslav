from operations import get_number_input, perform_operation
import logging  

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  
        format='%(asctime)s - %(levelname)s - %(message)s', 
        filename='calculator.log', 
        filemode='a',
        encoding='utf-8'
    )
    logging.info("--- СЕСІЯ: Калькулятор запущено ---")

def calculator():

    setup_logging() 

    supported_ops = ['+', '-', '*', '/']
    print("--- Калькулятор (Модульна версія) ---")
    print("Для завершення введіть: exit")

    while True:
        op = input(f"\nОберіть операцію ({', '.join(supported_ops)}) або 'exit': ").lower()

        if op == "exit":
            logging.info("--- СЕСІЯ: Програма завершена ---") 
            print("Програма завершена.")
            break

        if op not in supported_ops:
            print("Помилка! Невідома операція. Спробуйте ще раз.")
            continue

        a = get_number_input("Введіть перше число: ")
        b = get_number_input("Введіть друге число: ")

        result = perform_operation(op, a, b)
        
        log_message = f"Дані: ({a} {op} {b}) | Результат: {result}"
        logging.info(log_message)
        
        print("Результат:", result)

if __name__ == "__main__":
    calculator()