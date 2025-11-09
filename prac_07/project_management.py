"""
myguitars.py
Estimate time: 120 mins
Actual time:   mins
"""

import datetime
from operator import itemgetter
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
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        # elif choice == "d":
        #     display_projects(projects)
        # elif choice == "f":
        #     filter_projects(projects)
        # elif choice == "a":
        #     add_project(projects)
        # elif choice == "u":
        #     update_project(projects)

    save_choice = input("Would you like to save to projects.txt? ")
    if save_choice.lower().startswith("y"):
        save_projects("projects.txt", projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename="projects.txt"):
    """Load projects from a file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save projects to the file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)
    print(f"Projects saved to {filename}")

if __name__ == "__main__":
    main()
