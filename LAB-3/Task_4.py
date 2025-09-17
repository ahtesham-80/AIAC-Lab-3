def register_user(users_db):
    print("=== User Registration ===")
    while True:
        username = input("Enter a username: ").strip()
        if not username:
            print("Username cannot be empty. Please try again.")
            continue
        if username in users_db:
            print("Username already exists. Please choose another.")
            continue
        break
    while True:
        password = input("Enter a password: ").strip()
        if not password:
            print("Password cannot be empty. Please try again.")
            continue
        break
    users_db[username] = password
    print(f"User '{username}' registered successfully!\n")

def login_user(users_db):
    print("=== User Login ===")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if username in users_db and users_db[username] == password:
        print(f"Login successful! Welcome, {username}.\n")
        return True
    else:
        print("Invalid username or password. Please try again.\n")
        return False

if __name__ == "__main__":
    users_db = {}
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()
        if choice == '1':
            register_user(users_db)
        elif choice == '2':
            login_user(users_db)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")