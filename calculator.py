# calculator.py
# Простой калькулятор на Python с историей операций

def add(a, b):
    """Сложение"""
    return a + b

def subtract(a, b):
    """Вычитание"""
    return a - b

def multiply(a, b):
    """Умножение"""
    return a * b

def divide(a, b):
    """Деление"""
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def power(a, b):
    """Возведение в степень"""
    return a ** b

def show_history(history):
    """Показывает историю операций"""
    if not history:
        print("\n📝 История пуста")
        return
    
    print("\n📝 История операций:")
    for i, operation in enumerate(history, 1):
        print(f"{i}. {operation}")

def main():
    """Основная функция калькулятора"""
    history = []
    
    print("🧮 Добро пожаловать в Python калькулятор!")
    print("=" * 45)
    
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Возведение в степень (^)")
        print("6. Показать историю")
        print("0. Выход")
        
        choice = input("\nВаш выбор (0-6): ")
        
        if choice == '0':
            print("\n👋 До свидания!")
            break
        elif choice == '6':
            show_history(history)
            continue
        elif choice not in ['1', '2', '3', '4', '5']:
            print("❌ Ошибка: выберите число от 0 до 6")
            continue
        
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("❌ Ошибка: введите корректные числа!")
            continue
        
        result = None
        operation_symbol = ""
        
        if choice == '1':
            result = add(num1, num2)
            operation_symbol = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation_symbol = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation_symbol = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation_symbol = "/"
        elif choice == '5':
            result = power(num1, num2)
            operation_symbol = "^"
        
        # Форматируем вывод в зависимости от типа результата
        if isinstance(result, str):  # Если это ошибка (деление на ноль)
            print(f"\n❌ Результат: {result}")
            history_entry = f"{num1} {operation_symbol} {num2} = {result}"
        else:
            print(f"\n✅ Результат: {num1} {operation_symbol} {num2} = {result}")
            history_entry = f"{num1} {operation_symbol} {num2} = {result}"
        
        history.append(history_entry)

if __name__ == "__main__":
    main()
