def temperature_conversion():
    print("=== Temperature Conversion ===")
    print("Select the conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
        except ValueError:
            print("Invalid input. Please enter a valid number for temperature.")
    elif choice == '2':
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")
        except ValueError:
            print("Invalid input. Please enter a valid number for temperature.")
    else:
        print("Invalid choice. Please select 1 or 2.")

def calculator():
    """Simple calculator function"""
    print("=== Simple Calculator ===")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (1-4): ").strip()
        
        if operation == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero!")
        else:
            print("Invalid operation choice.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def display_info():
    """Function to display program information"""
    print("=== Program Information ===")
    print("This is a multi-function program that includes:")
    print("1. Temperature Conversion (Celsius ↔ Fahrenheit)")
    print("2. Simple Calculator (Basic arithmetic operations)")
    print("3. Program Information")
    print("4. Exit the program")
    print("\nSelect any option from the main menu to get started!")

def main_menu():
    """Main menu function that continues until user exits"""
    while True:
        print("\n" + "=" * 50)
        print("MULTI-FUNCTION PROGRAM")
        print("=" * 50)
        print("1. Temperature Conversion")
        print("2. Calculator")
        print("3. Program Information")
        print("4. Exit")
        print("-" * 50)
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            print("\n")
            temperature_conversion()
        elif choice == '2':
            print("\n")
            calculator()
        elif choice == '3':
            print("\n")
            display_info()
        elif choice == '4':
            print("\nThank you for using the Multi-Function Program!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
        
        # Ask if user wants to continue after each operation
        if choice != '4':
            print("\n" + "-" * 30)
            continue_choice = input("Press Enter to continue or 'q' to quit: ").strip().lower()
            if continue_choice == 'q':
                print("Thank you for using the Multi-Function Program!")
                print("Goodbye!")
                break

if __name__ == "__main__":
    main_menu()