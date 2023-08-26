# Bug tracking system 
import sys
import sqlite3 as sq
# creating a database
con = sq.connect("Bug_tracking_system")
cur = con.cursor()

# cur.execute("DROP TABLE IF EXISTS manager")
cur.execute("create table if not exists manager (empCode int primary key, name varchar(30) not null, email varchar(40) not null, emppassword varchar(20) not null,gender varchar(10), DOB varchar(20) not null,mobileNo bigint not null, role varchar(20) not null)")
con.commit()

def Add_emp_pannel():
    empCode = int(input("Enter the Manager Code: "))
    empName = input("Enter the Manager Name: ")
    empemail = input("Enter the Email: ")
    emppassword = input("Enter the password: ")
    gender = input("Enter the gender: ")
    DOB = input("Enter the Date of Birth: ")
    mobileNO = int(input("Enter the mobile number: "))
    role = input("Enter the Role: ")
    qry = "INSERT INTO manager VALUES (%d, '%s', '%s', '%s', '%s', '%s', %d, '%s')" % (
        empCode, empName, empemail, emppassword, gender, DOB, mobileNO, role)
    cur.execute(qry)
    con.commit()
    if cur.rowcount > 0:
        print("\nNew employee added...")
    else:
        print("Error in adding a new employee")
    input("\n\nPress Enter to continue")
# view manager
def view_all_manager():
    way = int(input("Enter the manager Code to view the details or enter 0 to get all the managers: "))
    if way == 0:
        qry = "SELECT * FROM manager WHERE role = 'manager'"
        cur.execute(qry)
        result = cur.fetchall()
        if len(result) > 0:
            print(" " * 94)
            print("%5s %30s %40s %20s %10s %12s %15s %20s" % (
                "empCode", "empName", "empemail", "emppassword", "gender", "DOB", "mobileNO", "role"))
            print(" " * 94)
            for row in result:
                print("%5d %30s %40s %20s %10s %12s %15d %20s" % (
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        else:
            print("No records found for managers.")
    else:
        qry = "SELECT * FROM manager WHERE empCode = ?"
        cur.execute(qry, (way,))
        row = cur.fetchone()
        if row:
            print(" " * 94)
            print("%5s %30s %40s %20s %10s %12s %15s %20s" % (
                "empCode", "empName", "empemail", "emppassword", "gender", "DOB", "mobileNO", "role"))
            print(" " * 94)
            print("%5d %30s %40s %20s %10s %12s %15d %20s" % (
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        else:
            print('No record found.')

    input("\n\nPress Enter to continue")
# delete manager
def delete_manager():
    id = input("Enter the Manager Code to be deleted: ")
    cur.execute("delete from manager where empcode = ?", (id,))
    con.commit()
    if cur.rowcount > 0:
        print("Record deleted.....")
    else:
        print("No data found....")
    input("\n\nPress Enter to continue")
# update manager
def update_manager_profile():
    id = int(input("Enter the Manager Code: "))
    cur.execute("SELECT * FROM manager WHERE empCode = ?", (id,))
    result = cur.fetchone()
    if result:
        while True:
            print("Enter 1 to update Name")
            print("Enter 2 to update email")
            print("Enter 3 to update DOB")
            print("Enter 4 to update mobile number")
            print("Enter 5 to update password")
            print("Enter 6 to gender")
            print("Enter 7 to role")
            print("Enter 8 to update All")
            print("Enter 9 to update Back")
            choice = int(input("Enter the choice: "))
            if choice == 1:
                name = input("Enter the Name: ")
                cur.execute("UPDATE manager SET name = ? WHERE empCode = ?", (name, id))
                con.commit()
                if cur.rowcount > 0:
                    print("Name updated Successfully....")
                else:
                    print("Error in updating the Name...")
            elif choice == 2:
                email = input("Enter the Email: ")
                cur.execute("UPDATE manager SET email = ? WHERE empCode = ?", (email, id))
                con.commit()
                if cur.rowcount > 0:
                    print("Email updated Successfully....")
                else:
                    print("Error in updating the Email...")
            elif choice == 3:
                dob = input("Enter the DOB: ")
                cur.execute("UPDATE manager SET DOB = ? WHERE empCode = ?", (dob, id))
                con.commit()
                if cur.rowcount > 0:
                    print("DOB updated Successfully....")
                else:
                    print("Error in updating the DOB...")
            elif choice == 4:
                mobileNo = input("Enter the Mobile number: ")
                cur.execute("UPDATE manager SET mobileNo = ? WHERE empCode = ?", (mobileNo, id))
                con.commit()
                if cur.rowcount > 0:
                    print("Mobile number updated Successfully....")
                else:
                    print("Error in updating the Mobile number...")
            elif choice == 5:
                password = input("Enter the password: ")
                cur.execute("UPDATE manager SET emppassword = ? WHERE empCode = ?", (password, id))
                con.commit()
                if cur.rowcount > 0:
                    print("Password updated Successfully....")
                else:
                    print("Error in updating the Password...")
            elif choice == 6:
                gender = input("Enter the gender: ")
                cur.execute("UPDATE manager SET gender = ? WHERE empCode = ?", (gender, id))
                con.commit()
                if cur.rowcount > 0:
                    print("Gender updated Successfully....")
                else:
                    print("Error in updating the Gender...")
            elif choice == 7:
                role = input("Enter the role: ")
                cur.execute("UPDATE manager SET role = ? WHERE empCode = ?", (role, id))
                con.commit()
                if cur.rowcount > 0:
                    print("Role updated Successfully....")
                else:
                    print("Error in updating the Role...")
            elif choice == 8:
                name = input("Enter the Name: ")
                email = input("Enter the Email: ")
                dob = input("Enter the DOB: ")
                mobileNo = input("Enter the Mobile number: ")
                password = input("Enter the password: ")
                gender = input("Enter the gender: ")
                role = input("Enter the role: ")
                cur.execute("UPDATE manager SET name = ?, email = ?, DOB = ?, mobileNo = ?, emppassword = ?, gender = ?, role = ? WHERE empCode = ?", (name, email, dob, mobileNo, password, gender, role, id))
                con.commit()
                if cur.rowcount > 0:
                    print("Record updated Successfully....")
                else:
                    print("Error in updating the record...")
            elif choice == 9:
                break
            else:
                print("Invalid choice")
        input("\n\nPress Enter to continue")
    else:
        print('No record found for the given Manager Code.')

