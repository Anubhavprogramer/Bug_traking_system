import manager as man
import projects as project
def Manager_pannel():
    print("You are now in manager Pannel, You can do various things......")
    print("1------Update Profile")
    print("2------Add project")
    print("3------View All project")
    print("4------Delete project")
    print("5------Update project")
    while True:
        manager_choice=int(input("Enter the Choice..."))
        match manager_choice:
            case 1:
                man.update_manager_profile()
            case 2:
                project.add_project()
            case 3:
                project.view_all()
            case 4:
                project.delete_project()
            case 5:
                project.update_project()
            case _:
                print("Invalid value......")