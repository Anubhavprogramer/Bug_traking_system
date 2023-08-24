import Employee as emp
import Bug_managering_part as bug
import sqlite3 as sq

# Create a database connection
con = sq.connect("Bug_tracking_system")
cur = con.cursor()

def employee_pannel():
    print("You are now in Manager Panel, You can do various things......")
    print("1------Update Profile")
    print("2------Add Bug's Report")
    print("3------View Bug's")
    print("4------Bug Detail’s")
    print("5------Update Bug status")
    print("6------EXIT")

    while True:
        try:
            manager_choice = int(input("Enter the Choice: "))

            if manager_choice == 1:
                emp.update_employee_profile()
                break
            elif manager_choice == 2:
                empcode = int(input("Enter the employee code for additional authentication: "))
                qry = "SELECT * FROM Employee WHERE empCode = ?"
                cur.execute(qry, (empcode,))
                row = cur.fetchone()
                if row is not None and row[6] == "Tester":
                    bug.add_bug_Report()  # Tester part
                else:
                    print("Sorry for interruption, but this task is assigned only for testers.")
                break
            elif manager_choice == 3:
                bug.view_bug()
                break
            elif manager_choice == 4:
                bug.view_bug()
                break
            elif manager_choice == 5:
                bug.update_status()
                break
            elif manager_choice == 6:
                confirm_exit = input("Are you sure you want to exit? (y/n): ")
                if confirm_exit.lower() == 'y':
                    print("Thank you")
                    break
            else:
                print("Invalid value......")
        except ValueError:
            print("Invalid input. Please enter a valid choice.")

    input("You are out of the Manager panel,\n press Enter to continue")

