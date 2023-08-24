import manager as man
import projects as project

def manager_panel():
    while True:
        print("You are now in Manager Panel. You can do various things...")
        print("1 - Update Profile")
        print("2 - Add Project")
        print("3 - View All Projects")
        print("4 - Delete Project")
        print("5 - Update Project")
        print("6 - Exit")

        manager_choice = input("Enter your choice: ")

        if manager_choice == '1':
            man.update_manager_profile()
        elif manager_choice == '2':
            project.add_project()
        elif manager_choice == '3':
            project.view_all()
        elif manager_choice == '4':
            project.delete_project()
        elif manager_choice == '5':
            project.update_project()
        elif manager_choice == '6':
            print("Thank you")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    input("You are out of the Manager panel. Press Enter to continue")
