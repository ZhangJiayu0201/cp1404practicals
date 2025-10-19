CODE_TO_COLOURS = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff", "alizarin crimson": "#e32636",
                   "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc", "antiquewhite": "#faebd7"}

print(CODE_TO_COLOURS)

name = input("Enter colour name: ").lower()
while name != "":
    try:
        print((CODE_TO_COLOURS[name]))
    except KeyError:
        print("Invalid colour name")
    state_code = input("Enter colour name: ").lower()
for k, name in CODE_TO_COLOURS.items():
    print(f"{k.title():16} is {name}")
