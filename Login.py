import sys
import sqlite3 as sq
import Manager_pannel as manager_pannel
import Employee_pannel as employee_pannel
import Admain as ad

# Creating a database connection and cursor
print("-------BUG TRACKING SYSTEM-------")
con = sq.connect("Bug_tracking_system")
cur = con.cursor()

# Creating the Employee table if it doesn't exist
cur.execute("CREATE TABLE IF NOT EXISTS Employee (empCode INTEGER PRIMARY KEY, name VARCHAR(30) NOT NULL, email VARCHAR(40) NOT NULL, emppassword VARCHAR(20) NOT NULL, DOB VARCHAR(20) NOT NULL, mobileNo BIGINT NOT NULL, role VARCHAR(20) NOT NULL)")
con.commit()

# A dictionary for user database (you can replace this with a real database)
user_database = {
    'Admin': '123',
}

# Function to perform user login
def login():
    username = input("Enter your Employee Code: ")
    password = input("Enter your password: ")

    qry = "SELECT * FROM Employee WHERE empCode = ?"
    cur.execute(qry, (username,))
    row = cur.fetchone()
    if (username in user_database and user_database[username] == password):
        print("Login successful!")
        ad.admain_pannel()
    elif row is not None and row[3] == password:
        role = row[6]
        if role == "Manager":
            manager_pannel.manager_panel()
        elif role == "Employee":
            employee_pannel.employee_pannel()
        
        elif role == "admain":
            ad.admain_pannel()
        else:
            print("Invalid role.")
    elif username in user_database and user_database[username] == password:
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
def main():
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

    # Close the database connection when done
    con.close()

if __name__ == "__main__":
    main()  # Call the main function when the script is executed
