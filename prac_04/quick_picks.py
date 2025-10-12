import random

NUMBERS_IN_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

pick_times = int(input("How many quick picks?"))

for i in range(pick_times):
    numbers = []
    while len(numbers) < NUMBERS_IN_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)

    print(" ".join(f"{num:2}" for num in sorted(numbers)))
