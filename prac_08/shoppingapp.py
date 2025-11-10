from kivy.app import App

class ShoppingApp(App):
    total = 0

    def add_to_total(self, price):
        self.total += price
        self.root.ids.total_label.text = f"Total: {self.total}"

    def clear_total(self):
        self.total = 0
        self.root.ids.total_label.text = "Total: 0"


if __name__ == "__main__":
    ShoppingApp().run()
