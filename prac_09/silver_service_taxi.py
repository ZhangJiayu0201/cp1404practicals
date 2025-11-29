
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with additional flagfall and fanciness multiplier."""

    flagfall = 4.50  # extra charge per fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        base_fare = super().get_fare()
        return base_fare + self.flagfall

