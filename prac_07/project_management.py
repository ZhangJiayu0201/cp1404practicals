"""
myguitars.py
Estimate time: 150 mins
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
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)

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


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects: ")
    for project in incomplete:
        print(" ", project)

    print("Completed projects: ")
    for project in complete:
        print(" ", project)


def filter_projects(projects):
    """Filter projects start after given date and display."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    project_dicts = [
        {"project": p, "start_date": p.start_date} for p in projects if p.start_date >= filter_date]

    project_dicts.sort(key=itemgetter("start_date"))

    for item in project_dicts:
        print(item["project"])


def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, completion))


def update_project(projects):
    """Update completion % and priority of a project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_completion = input("New Percentage: ")
    if new_completion:
        project.completion_percentage = int(new_completion)
    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)


if __name__ == "__main__":
    main()
