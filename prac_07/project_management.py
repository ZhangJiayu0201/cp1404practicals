"""
myguitars.py
Estimate time: 120 mins
Actual time:   mins
"""


from project import Project


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects()

    menu = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""

    choice = ""
    while choice.lower() != "q":
        print(menu)
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Filename to load from: ")

        elif choice == "s":
            filename = input("Filename to save to: ")

        elif choice == "d":

        elif choice == "f":

        elif choice == "a":

        elif choice == "u":


    save_choice = input("Would you like to save to projects.txt? ")
    if save_choice.lower().startswith("y"):
        save_projects("projects.txt", projects)
    print("Thank you for using custom-built project management software.")

