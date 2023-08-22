# Bug Tracking system
import manager as manager;
import Employee as employee
def admain_pannel():
    print("You are in Admain pannel")
    print("1 for Manager")
    print("2 for Employee")
    print("3 for View All project")
    print("4 for View Bug's List")
    print("5 for Exit")
    while True:
        Admain_choice=input("Entre the choice")
        if Admain_choice=='1':
            admain_manager_pannel()
        elif Admain_choice=='2':
            admain_Employee_pannel()
        elif Admain_choice=='3':
            View_All_Project()
        elif Admain_choice=='4':
            View_Bug_Reports()
        elif Admain_choice=='5':
            break
        else:
            print("Invalid option")
# manager
def admain_manager_pannel():
    print("You are now in Manager Pannel You can do various things")
    print("Add Manager Account ----->1")
    print("View Manger Account ----->2")
    print("Delete Manager ----->3")
    print("Update Manager Detail's ----->4")
    print("Exit Manager-Pannel  ----->5")

    while True:
        Admain_manager_choice=input("Entre the choice")
        if Admain_manager_choice=='1':
           manager.Add_emp_pannel()
        elif Admain_manager_choice=='2':
            manager.view_all_manager()
        elif Admain_manager_choice=='3':
            manager.delete_manager()
        elif Admain_manager_choice=='4':
            manager.update_manager_profile()
        elif Admain_manager_choice=='5':
            break
        else:
            print("Invalid option")

            # Employee
def admain_Employee_pannel():
    print("You are now in Employee Pannel You can do various things")
    print("Add Employee Account ----->1")
    print("View Employee's Account ----->2")
    print("Delete Employee Account ----->3")
    print("Update Employee Detail's ----->4")
    print("Exit Employee-Pannel  ----->5")
   
    while True:
        Admain_Employee_choice=input("Entre the choice")
        if Admain_Employee_choice=='1':
            employee.Add_emp_pannel()
        elif Admain_employee_choice=='2':
            admain_Employee_pannel()
        elif Admain_employee_choice=='3':
            View_All_Project()
        elif Admain_employee_choice=='4':
            View_Bug_Reports()
        elif Admain_employee_choice=='5':
            break
        else:
            print("Invalid option")
# view all project
def View_All_Project():
    pass

# view bug report
def View_Bug_Reports():
    pass





