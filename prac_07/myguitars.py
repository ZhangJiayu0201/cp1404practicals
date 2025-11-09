"""
myguitars.py
Estimate time: 30 mins
Actual time:  mins
"""


from guitar import Guitar


def main():
    guitars = load_guitars()
    guitars.sort()
    print("Guitars sorted by Year")
    for guitar in guitars:
        print(guitar)


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


if __name__ == "__main__":
    main()
