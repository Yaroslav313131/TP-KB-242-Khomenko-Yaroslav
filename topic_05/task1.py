import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Нічия!"
    elif (user_choice == "stone" and computer_choice == "scissor"):
        return "Ви перемогли!"
    elif (user_choice == "scissor" and computer_choice == "paper"):
        return "Ви перемогли!"
    elif (user_choice == "paper" and computer_choice == "stone"):
        return "Ви перемогли!"
    else:
        return "Комп'ютер переміг!"

def play_game():
    options = ["stone", "scissor", "paper"]
    print("--- Початок гри Камінь, Ножиці, Папір ---")
    print("Правила: Камінь > Ножиці | Ножиці > Папір | Папір > Камінь")
    print("Для завершення гри введіть 'exit'.")

    while True:
        user_input = input(f"\nВаш хід ({', '.join(options)} або exit): ").lower()
        
        if user_input == "exit":
            print("Дякуємо за гру! Програма завершена.")
            break
        
        if user_input not in options:
            print(f"Помилка! Будь ласка, введіть одне зі значень: {', '.join(options)}.")
            continue
        
        computer_choice = random.choice(options)
        
        print(f"Ваш хід:     {user_input.capitalize()}")
        print(f"Хід комп'ютера: {computer_choice.capitalize()}")
        
        result = determine_winner(user_input, computer_choice)
        print(f"*** Результат: {result} ***")

play_game()