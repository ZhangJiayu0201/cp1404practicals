"""
guitar.py
Estimate time: 20 mins
Actual time: 16 mins
"""
CURRENT_YEAR = 2022
VINTAGE_YEAR = 50


class Guitar:
    """Represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return how old the guitar is."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return the guitar is more than 50 years old or not."""
        return self.get_age() >= VINTAGE_YEAR

    def __str__(self):
        """Return string of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Return the result of compare guitars by year."""
        return self.year < other.year

