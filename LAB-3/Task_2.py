def sort_numbers_menu():
    print("Enter numbers separated by spaces:")
    try:
        numbers = list(map(int, input().split()))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    print("\nSelect an option:")
    print("1. Sort in ascending order")
    print("2. Sort in descending order")
    print("3. Show only odd numbers")
    print("4. Show only even numbers")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        sorted_numbers = sorted(numbers)
        print("Ascending order:", sorted_numbers)
    elif choice == '2':
        sorted_numbers = sorted(numbers, reverse=True)
        print("Descending order:", sorted_numbers)
    elif choice == '3':
        odd_numbers = [num for num in numbers if num % 2 != 0]
        print("Odd numbers:", odd_numbers)
    elif choice == '4':
        even_numbers = [num for num in numbers if num % 2 == 0]
        print("Even numbers:", even_numbers)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    sort_numbers_menu()