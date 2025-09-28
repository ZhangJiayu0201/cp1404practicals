"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)
    random_score = random.randint(0, 100)
    random_result = get_result(random_score)
    print(random_score, random_result)


def get_result(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
