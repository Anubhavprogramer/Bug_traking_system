# User database (You can replace this with a real database)
import Admain as ad
import sys
import sqlite3 as sq
import Manager_pannel as manager_pannel
# creating a database
con = sq.connect("Bug_tracking_system")
cur = con.cursor()
cur.execute("create table if not exists Employee (empCode int primary key, name varchar(30) not null, email varchar(40) not null, emppassword varchar(20) not null, DOB varchar(20) not null,mobileNo bigint not null, role varchar(20) not null)")
con.commit()
user_database = {
    'Admain': '123',
}

# Function to perform user login
def login():
    username = input("Enter your Employee Code: ")
    password = input("Enter your password: ")

    qry = "SELECT * FROM Employee WHERE empCode = ?"
    cur.execute(qry, (username))
    row = cur.fetchone()

    if (username in user_database and user_database[username] == password):
        print("Login successful!")
        ad.admain_pannel()
    elif row[3]==password:
        match(row[7]):
            case "Manager":
                pass

            case "Employee":
                pass
            case "Tester":
                pass
        
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
