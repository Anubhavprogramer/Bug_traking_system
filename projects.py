# poject database and functions
import sys
import sqlite3 as sq

con = sq.connect("Bug_tracking_system")
cur = con.cursor()
cur.execute("create table if not exists Project (projectID int primary key, projectname varchar(30) not null, SDate varchar(30) not null, EDate varchar(30) , projectDec varchar(200) not null)")
con.commit()

def add_project():
    print("Enter the Data of Project")
    projectid = int(input("Enter the Project ID: "))
    projectname = input("Enter the Project Name: ")
    sdate = input("Enter the start Date: ")
    edate = input("Enter the end Date: ")
    prodec = input("Enter the descreption of project: ")

    qry = "INSERT INTO Employee VALUES (%d, '%s', '%s', '%s', '%s')" % (
        projectid, projectname, sdate, edate, prodec)
    cur.execute(qry)
    con.commit()
    if cur.rowcount > 0:
        print("\nNew project added...")
    else:
        print("Error in adding a new project")
    input("\n\nPress Enter to continue")

def view_all():
    cur.execute("SELECT * from Project")
    result = cur.fetchall()
    if len(result) > 0:
        print(" " * 94)
        print("%5s %30s %40s %20s %10s %12s %15s %20s" % (
            "projectid", "projectname", "sdate", "edate", "prodec"))
        print(" " * 94)
        for row in result:
            print("%5d %30s %40s %20s %10s " % (
                row[0], row[1], row[2], row[3], row[4]))
    else:
        print("No records found for Project.")

def delete_project():
    initial = cur.rowcount()
    projectid= input("Enter the project ID which you want to delete: ")
    cur.execute("delete from Project where projectID is ",projectid)
    con.commit()
    final = cur.rowcount()
    if initial-1 == final:
        print("Desired project has been deleted successfully..")
    else:
        print("Error occurred in deleting the Project ")
    input("\n\nPress Enter to continue")

def update_project():
    projectid= input("Enter the project ID which you want to Update: ")
    cur.execute("select form Project where projectID is ",(projectid))
    result = cur.fetchone()
    if result:
        print("Enter 1 to update project name")
        print("Enter 2 to update start date")
        print("Enter 3 to update end date")
        print("Enter 4 to update project description")
        print("Enter 5 to exit")
        while True:
            choice = int(input("Enter the choice: "))

            match choice:
                case 1:
                    name = input("Enter the Project Name: ")
                    cur.execute("UPDATE Project SET projectname = ? WHERE projectID = ?", (name, id))
                    con.commit()
                    if cur.rowcount > 0:
                        print("Name updated Successfully....")
                    else:
                        print("Error in updating the Name...")
                    break

                case 2:
                    name = input("Enter the new start date: ")
                    cur.execute("UPDATE Project SET SDate = ? WHERE projectID = ?", (name, id))
                    con.commit()
                    if cur.rowcount > 0:
                        print("Name updated Successfully....")
                    else:
                        print("Error in updating the Name...")
                    break

                case 3:
                    name = input("Enter the new end date: ")
                    cur.execute("UPDATE Project SET EDate = ? WHERE projectID = ?", (name, id))
                    con.commit()
                    if cur.rowcount > 0:
                        print("Name updated Successfully....")
                    else:
                        print("Error in updating the Name...")
                    break

                case 4:
                    name = input("Enter the new project descreption: ")
                    cur.execute("UPDATE Project SET projectDec = ? WHERE projectID = ?", (name, id))
                    con.commit()
                    if cur.rowcount > 0:
                        print("Name updated Successfully....")
                    else:
                        print("Error in updating the Name...")
                    break

                case 5:
                    break

                case _:
                    print("Invalid choice..")
                    break
    else:
        print("Error in finding the Data")
    input("your are out press Enter to continue")

cur.close()