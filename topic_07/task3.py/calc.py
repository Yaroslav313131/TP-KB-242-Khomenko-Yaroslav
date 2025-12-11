from operations import Calculator
def main():
    try:
        my_calculator = Calculator()
        my_calculator.run()
    except Exception as e:
        print(f"\nКритична помилка програми: {e}")

if __name__ == "__main__":
    main()