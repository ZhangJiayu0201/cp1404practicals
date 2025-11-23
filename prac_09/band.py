

class Band:
    """Band class has many musicians."""

    def __init__(self, name=""):
        """Initialise a Band with name and musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return the Band and its musicians."""
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return each musician plays."""
        return "\n".join(musician.play() for musician in self.musicians)
