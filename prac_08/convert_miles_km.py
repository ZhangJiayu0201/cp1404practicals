"""
convert_miles_km.py
Estimate time: 60 mins
Actual time: 66 mins
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKilometersApp(App):
    """ MilesToKilometersApp is a Kivy App for converting miles to kilometres """
    output_text = StringProperty("0.0")

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ Calculation, output result to string """
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.output_text = str(result)

    def handle_increment(self, change):
        """Process increments (increments or decreases)"""
        value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_valid_miles(self):
        """Get valid input from text entry widget, if error return 0"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometersApp().run()
