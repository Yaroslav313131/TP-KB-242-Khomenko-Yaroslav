import requests

from datetime import datetime

API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"

SUPPORTED_CURRENCIES = ["USD", "EUR", "PLN"]

def fetch_exchange_rates(api_url):
    print("🔌 Запит актуальних курсів НБУ...")
    try:
        # Виконання GET-запиту до API
        response = requests.get(api_url)
        # Перевірка, чи був запит успішним (код 200)
        response.raise_for_status() 
        
        # Перетворення JSON-відповіді на список словників
        data = response.json()
        
        rates = {}
        # Фільтруємо та зберігаємо лише потрібні нам курси
        for item in data:
            cc = item.get("cc")
            rate = item.get("rate")
            if cc and rate and cc in SUPPORTED_CURRENCIES:
                rates[cc] = rate
        
        # Перевіряємо, чи отримали ми всі необхідні курси
        if len(rates) == len(SUPPORTED_CURRENCIES):
            print(f"✅ Курси успішно отримано за даними НБУ на {datetime.now().strftime('%d.%m.%Y')}.")
            return rates
        else:
            print("⚠️ Помилка: Не вдалося отримати всі необхідні курси валют з API.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ Помилка при виконанні запиту до API НБУ: {e}")
        return None
    except Exception as e:
        print(f"❌ Невідома помилка при обробці даних: {e}")
        return None

def get_number_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            amount = float(user_input)
            if amount > 0:
                return amount
            else:
                print("Помилка! Сума має бути додатним числом.")
        except ValueError:
            print("Помилка! Будь ласка, введіть коректне числове значення.")

def currency_converter():
    exchange_rates = fetch_exchange_rates(API_URL)
    
    if not exchange_rates:
        print("\nНеможливо продовжити роботу без актуальних курсів. Спробуйте пізніше.")
        return

    print("\n--- Конвертер Валют в UAH ---")
    print(f"Підтримувані валюти: {', '.join(SUPPORTED_CURRENCIES)}")
    
    while True:
        currency_type = input("\nВведіть код валюти (USD, EUR, PLN) або 'exit': ").upper()
        
        if currency_type == "EXIT":
            print("Програма завершена.")
            break
            
        if currency_type not in SUPPORTED_CURRENCIES:
            print(f"Помилка! Підтримуються лише {', '.join(SUPPORTED_CURRENCIES)}.")
            continue
            
        amount = get_number_input(f"Введіть суму в {currency_type}: ")
        
        # Конвертація
        rate = exchange_rates.get(currency_type)
        if rate:
            # Конвертація: Сума * Курс_НБУ
            uah_amount = amount * rate
            
            print("--- Результат ---")
            print(f"{amount:.2f} {currency_type} = {uah_amount:.2f} UAH (Курс НБУ: {rate:.4f})")
            print("-----------------")
        else:
            print(f"❌ Помилка: Курс для {currency_type} не знайдено.")
currency_converter()