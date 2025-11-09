"""
guitar_test.py
Estimate time: 30 mins
Actual time: 24 mins
"""

from guitar import Guitar


def main():
    """Demo test code to show how to use guitar class."""
    gibson = Guitar("Gibson L-5 CES", 1922, 1995)
    another_guitar = Guitar("Another Guitar", 2013, 1983)

    guitars = [gibson, another_guitar]

    for guitar in guitars:
        print(guitar.get_age())
        print(guitar.is_vintage())

    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")

    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

main()
