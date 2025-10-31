"""
languages.py
Estimate time: 30 mins
Actual time: 27 mins
"""

from programming_language import ProgrammingLanguage


def main():
    """Demo test code to show how to use programmingLanguage class."""
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    c_plus = ProgrammingLanguage("C++", "Static", False, 1983)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)

    languages = [java, c_plus, python, ruby, visual_basic]

    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
