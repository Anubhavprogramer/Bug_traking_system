# User database (You can replace this with a real database)
import Admain as ad
user_database = {
    'Admain': '123',
    'user2': 'password2',
    'user3': 'password3'
}

# Function to perform user login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_database and user_database[username] == password:
        print("Login successful!")
        ad.admain_pannel()
        
    else:
        print("Login failed. Invalid username or password.")

# Main menu function
def main_menu():
    print("\nMenu:")
    print("1. Login")
    print("2. Exit")

# Main program loop
while True:
    main_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        login()
    elif choice == '2':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
