import math

class RPNProcessor:
    def __init__(self):
        self.priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def extract_tokens(self, expression: str):
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]

            if char.isspace():
                i += 1
                continue

            if char.isdigit() or char == '.':
                buffer = ""
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    buffer += expression[i]
                    i += 1
                tokens.append(buffer)
                continue

            if char in "+-*/^()":
                if char == '-' and (not tokens or tokens[-1] in "+-*/^("):
                    buffer = "-"
                    i += 1
                    while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                        buffer += expression[i]
                        i += 1
                    tokens.append(buffer)
                    continue
                
                tokens.append(char)
                i += 1
                continue
            
            raise ValueError(f"Виявлено недопустимий символ: {char}")
        return tokens

    def convert_to_rpn(self, tokens):
        rpn_output = []
        op_stack = []

        for token in tokens:
            if token.replace('.', '', 1).lstrip('-').isdigit():
                rpn_output.append(token)
            
            elif token == '(':
                op_stack.append(token)
            
            elif token == ')':
                while op_stack and op_stack[-1] != '(':
                    rpn_output.append(op_stack.pop())
                if op_stack:
                    op_stack.pop() 
            
            elif token in self.priority:
                while (op_stack and op_stack[-1] != '(' and 
                       self.priority.get(op_stack[-1], 0) >= self.priority[token]):
                    rpn_output.append(op_stack.pop())
                op_stack.append(token)

        while op_stack:
            rpn_output.append(op_stack.pop())
        
        return rpn_output

    def calculate(self, rpn_tokens):
        calc_stack = []

        for token in rpn_tokens:
            if token.replace('.', '', 1).lstrip('-').isdigit():
                calc_stack.append(float(token))
            else:
                if len(calc_stack) < 2:
                    raise ValueError("Помилка в структурі виразу")
                
                right = calc_stack.pop()
                left = calc_stack.pop()
                
                if token == '+': calc_stack.append(left + right)
                elif token == '-': calc_stack.append(left - right)
                elif token == '*': calc_stack.append(left * right)
                elif token == '/':
                    if right == 0: raise ZeroDivisionError("Ділення на нуль!")
                    calc_stack.append(left / right)
                elif token == '^': calc_stack.append(math.pow(left, right))

        return calc_stack[0] if calc_stack else 0

def main():
    processor = RPNProcessor()
    print("Лабораторна робота: Обчислення через ЗПЗ")
    user_input = input("Введіть математичний вираз: ")

    try:
        tokens = processor.extract_tokens(user_input)
        
        rpn = processor.convert_to_rpn(tokens)
        print(f"\n[1] Зворотний польський запис: {' '.join(rpn)}")

        result = processor.calculate(rpn)
        
        formatted_res = f"{result:g}" 
        print(f"[2] Результат обчислення: {formatted_res}")

    except Exception as error:
        print(f"Виникла помилка: {error}")

if __name__ == "__main__":
    main()