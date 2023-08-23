# poject database and functions
import sys
import sqlite3 as sq

con = sq.connect("Bug_tracking_system")
cur = con.cursor()
cur.execute("create table if not exists Project (projectID int primary key, projectname varchar(30) not null, SDate varchar(30) not null, EDate varchar(30) , projectDec varchar(200) not null")
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