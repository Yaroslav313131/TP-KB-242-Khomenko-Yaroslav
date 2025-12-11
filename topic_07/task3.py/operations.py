import logging
from functions import add, sub, mul, div 

class Calculator:

    SUPPORTED_OPS = {'+': add, '-': sub, '*': mul, '/': div}

    def __init__(self, log_file='calculator.log'):
        self.log_file = log_file
        self._setup_logging()
        self.log.info("--- СЕСІЯ: Калькулятор запущено ---")

    def _setup_logging(self):
        self.log = logging.getLogger('CalculatorLog')
        self.log.setLevel(logging.INFO)
        
        if not self.log.handlers:
            file_handler = logging.FileHandler(self.log_file, mode='a', encoding='utf-8')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.log.addHandler(file_handler)

    def get_number_input(self, prompt):
        while True:
            try:
                user_input = input(prompt)
                return float(user_input)
            except ValueError:
                print("Помилка! Будь ласка, введіть коректне числове значення.")

    def perform_operation(self, op, a, b):
        operation_func = self.SUPPORTED_OPS.get(op)
        if operation_func:
            return operation_func(a, b)
        else:
            return "Помилка! Невідома операція."

    def run(self):
        print("--- Калькулятор  ---")
        print("Для завершення введіть: exit")

        while True:
            ops_list = list(self.SUPPORTED_OPS.keys())
            op = input(f"\nОберіть операцію ({', '.join(ops_list)}) або 'exit': ").lower()

            if op == "exit":
                self.log.info("--- СЕСІЯ: Програма завершена ---") 
                print("Програма завершена.")
                break

            if op not in ops_list:
                print("Помилка! Невідома операція. Спробуйте ще раз.")
                continue

            a = self.get_number_input("Введіть перше число: ")
            b = self.get_number_input("Введіть друге число: ")

            result = self.perform_operation(op, a, b)
            
            log_message = f"Дані: ({a} {op} {b}) | Результат: {result}"
            self.log.info(log_message)
            
            print("Результат:", result)