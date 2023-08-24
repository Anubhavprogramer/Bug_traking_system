import sys
import sqlite3 as sq

con = sq.connect("Bug_tracking_system")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS BugType (bugCode INTEGER PRIMARY KEY, bugCategory VARCHAR(30) NOT NULL, bugSeverity VARCHAR(30) NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS BugReport (bugNO INTEGER PRIMARY KEY, bugCode INTEGER NOT NULL, ProjectID INTEGER, TCode INTEGER, ECode INTEGER, status VARCHAR(20), bugDes VARCHAR(100))")

con.commit()

def view_bug():
    way = input('If you want to see all bug details, press "0000"; otherwise, enter the Bug Code: ')

    if way == "0000":
        # Fetch and display BugType records
        cur.execute("SELECT * FROM BugType")
        result = cur.fetchall()

        if len(result) > 0:
            print("%5s %30s %40s " % (
                "Bug Code", "Bug Category", "Bug Severity"))
            for row in result:
                print("%5d %30s %40s  " % (
                    row[0], row[1], row[2]))
        else:
            print("No records found for BugType.")

        # Fetch and display BugReport records
        cur.execute("SELECT * FROM BugReport")
        result2 = cur.fetchall()

        if len(result2) > 0:
            print("%5s %10s %10s %10s %10s %20s %40s " % (
                "Bug No.", "Bug Code", "ProjectID", "TCode", "ECode", "Status", "Bug Description"))
            for row in result2:
                print("%5d %10d %10d %10d %10d %20s %40s " % (
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        else:
            print("No records found for BugReport.")
    else:
        try:
            bug_code = int(way)
            cur.execute("SELECT * FROM BugReport WHERE bugCode = ?", (bug_code,))
            result3 = cur.fetchall()

            if len(result3) > 0:
                print("%5s %10s %10s %10s %10s %20s %40s " % (
                    "Bug No.", "Bug Code", "ProjectID", "TCode", "ECode", "Status", "Bug Description"))
                for row in result3:
                    print("%5d %10d %10d %10d %10d %20s %40s " % (
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            else:
                print(f"No records found for Bug with Code {bug_code}.")
        except ValueError:
            print("Invalid input. Please enter a valid Bug Code.")

# Function to update bug status
def update_status():
    try:
        bugcode = int(input("Enter the Bug Code for which you want to change the status: "))
        cur.execute("SELECT status FROM BugReport WHERE bugCode = ?", (bugcode,))
        existing_status = cur.fetchone()

        if existing_status:
            new_status = input("Enter the new status: ")
            cur.execute("UPDATE BugReport SET status = ? WHERE bugCode = ?", (new_status, bugcode))
            con.commit()
            print(f"Status for Bug with Code {bugcode} has been updated to: {new_status}")
        else:
            print(f"No bug found with Code {bugcode}. Please enter a valid Bug Code.")
    except ValueError:
        print("Invalid input. Please enter a valid Bug Code.")

# Function to add a bug report
def add_bug_Report():
    bug_code = int(input("Enter Bug Code: "))
    project_id = int(input("Enter Project ID: "))
    t_code = int(input("Enter TCode: "))
    e_code = int(input("Enter ECode: "))
    status = input("Enter Status: ")
    bug_description = input("Enter Bug Description: ")

    try:
        cur.execute("INSERT INTO BugReport (bugCode, ProjectID, TCode, ECode, status, bugDes) VALUES (?, ?, ?, ?, ?, ?)",
                    (bug_code, project_id, t_code, e_code, status, bug_description))
        con.commit()
        print("Bug Report added successfully!")
    except sq.IntegrityError:
        print("Error: Bug Code already exists. Please choose a unique Bug Code.")
