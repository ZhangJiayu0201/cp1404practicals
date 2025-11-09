"""
project.py
Estimate time: 30 mins
Actual time: 24 mins
"""


class Project:
    """Represent a project."""
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Initialize project data."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        """Return string of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Return priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return project fully completed."""
        return self.completion == 100
