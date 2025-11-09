"""
my guitars.py
Estimate time: 35 mins
Actual time:  28 mins
"""


from guitar import Guitar


def main():
    guitars = load_guitars()
    guitars.sort()

    print("Guitars sorted by Year")
    for guitar in guitars:
        print(guitar)
    guitars = add_new_guitars(guitars)
    save_guitars(guitars)


def load_guitars(filename="guitars.csv"):
    """Read guitars from a file and return a list."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def add_new_guitars(guitars):
    """Add guitar information based on user input."""
    print("Enter your guitar:")
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ").strip()
    return guitars


def save_guitars(guitars, filename="guitars.csv"):
    """Write all guitar information back to the file."""
    with open(filename, "w") as in_file:
        for guitar in guitars:
            in_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()
