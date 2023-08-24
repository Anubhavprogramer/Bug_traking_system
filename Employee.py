import sqlite3 as sq

# Create a database connection
con = sq.connect("Bug_tracking_system")
cur = con.cursor()

def add_employee():
    # Get employee details from user
    empCode = int(input("Enter the Employee Code: "))
    empName = input("Enter the Employee Name: ")
    empEmail = input("Enter the Email: ")
    empPassword = input("Enter the Password: ")
    gender = input("Enter the Gender: ")
    DOB = input("Enter the Date of Birth: ")
    mobileNo = int(input("Enter the Mobile Number: "))
    role = input("Enter the Role: ")

    # Use parameterized query to insert employee data
    try:
        cur.execute("INSERT INTO Employee (empCode, name, email, emppassword, gender, DOB, mobileNo, role) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, role))
        con.commit()
        print("Employee added successfully!")
    except sq.IntegrityError:
        print("Error: Employee with the same code already exists. Please choose a unique code.")

def view_all_employees():
    way = int(input("Enter the Employee Code to view details or enter 0 to get all employees: "))
    if way == 0:
        qry = "SELECT * FROM Employee WHERE role = 'Employee'"
        cur.execute(qry)
        result = cur.fetchall()
        if len(result) > 0:
            # Print employee details in a formatted table
            print(" " * 94)
            print("%5s %30s %40s %20s %10s %12s %15s %20s" % (
                "empCode", "empName", "empEmail", "empPassword", "gender", "DOB", "mobileNo", "role"))
            print(" " * 94)
            for row in result:
                print("%5d %30s %40s %20s %10s %12s %15d %20s" % (
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        else:
            print("No records found for employees.")
    else:
        qry = "SELECT * FROM Employee WHERE empCode = ?"
        cur.execute(qry, (way,))
        row = cur.fetchone()
        if row:
            # Print the employee details
            print(" " * 94)
            print("%5s %30s %40s %20s %10s %12s %15s %20s" % (
                "empCode", "empName", "empEmail", "empPassword", "gender", "DOB", "mobileNo", "role"))
            print(" " * 94)
            print("%5d %30s %40s %20s %10s %12s %15d %20s" % (
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        else:
            print('No record found for the given employee Code.')

def delete_employee():
    id = input("Enter the employee Code to be deleted: ")
    cur.execute("DELETE FROM Employee WHERE empCode = ?", (id,))
    con.commit()
    if cur.rowcount > 0:
        print("Record deleted.")
    else:
        print("No data found for the given employee Code.")

def update_employee_profile():
    id = int(input("Enter the employee Code: "))
    cur.execute("SELECT * FROM Employee WHERE empCode = ?", (id,))
    result = cur.fetchone()
    if result:
        while True:
            print("Choose what to update:")
            print("1. Name")
            print("2. Email")
            print("3. Date of Birth")
            print("4. Mobile Number")
            print("5. Password")
            print("6. Gender")
            print("7. Role")
            print("8. Update All")
            print("9. Back to Menu")
            choice = int(input("Enter the choice: "))
            if choice == 1:
                name = input("Enter the Name: ")
                cur.execute("UPDATE Employee SET name = ? WHERE empCode = ?", (name, id))
            elif choice == 2:
                email = input("Enter the Email: ")
                cur.execute("UPDATE Employee SET email = ? WHERE empCode = ?", (email, id))
            elif choice == 3:
                dob = input("Enter the Date of Birth: ")
                cur.execute("UPDATE Employee SET DOB = ? WHERE empCode = ?", (dob, id))
            elif choice == 4:
                mobileNo = int(input("Enter the Mobile Number: "))
                cur.execute("UPDATE Employee SET mobileNo = ? WHERE empCode = ?", (mobileNo, id))
            elif choice == 5:
                password = input("Enter the Password: ")
                cur.execute("UPDATE Employee SET emppassword = ? WHERE empCode = ?", (password, id))
            elif choice == 6:
                gender = input("Enter the Gender: ")
                cur.execute("UPDATE Employee SET gender = ? WHERE empCode = ?", (gender, id))
            elif choice == 7:
                role = input("Enter the Role: ")
                cur.execute("UPDATE Employee SET role = ? WHERE empCode = ?", (role, id))
            elif choice == 8:
                name = input("Enter the Name: ")
                email = input("Enter the Email: ")
                dob = input("Enter the Date of Birth: ")
                mobileNo = int(input("Enter the Mobile Number: "))
                password = input("Enter the Password: ")
                gender = input("Enter the Gender: ")
                role = input("Enter the Role: ")
                cur.execute("UPDATE Employee SET name = ?, email = ?, DOB = ?, mobileNo = ?, emppassword = ?, gender = ?, role = ? WHERE empCode = ?", (name, email, dob, mobileNo, password, gender, role, id))
            elif choice == 9:
                break
            else:
                print("Invalid choice")
            con.commit()
            print("Record updated successfully.")
    else:
        print('No record found for the given employee Code.')

# Main menu
while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Delete Employee")
    print("4. Update Employee Profile")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_all_employees()
    elif choice == '3':
        delete_employee()
    elif choice == '4':
        update_employee_profile()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
    input("\nPress Enter to continue...")
