# print("test")
#
#
# def fn(x, y):
#     z = x + y
#
#
# print(fn(1, 2))
#
#

# def question_4():
#     # write a program to read a file and print only the lines that start with a #. The user should enter the filename
#     filename = input("Enter the filename: ")
#     infile = open(filename, "r")
#     for line in infile:
#         if line.startswith("#"):
#             print(line.rstrip())
#     infile.close()
#
#
# question_4()
#
# s = "\tPython, Monty \n"
# print(s)
# print(len(s))
# print(s[1], ".", sep=" ")
# print(s.strip(), ".", sep="")
# s = s.replace(" ","*")
# print(s)
# print(s.lstrip(), ".", sep="")
# print(s.strip().split(","))
# print(list(s.strip()))


# name_list = ["Asda", "Basd", "Casd", "Dasd"]
# # write code that creates files from a list of strings.
# # Each file named with the value of the string. Write the string to the file.
# for i in range(len(name_list)):
#     with open(f"{name_list[i]}.txt", "w") as out_file:
#         print(f"{i+1} {name_list[i]}", file=out_file)

# for name in name_list:
#     filename = name + ".txt"
#     with open(filename, "w") as file:
#         file.write(name)

# with open("A.txt", "r") as in_file:
#     lines = in_file.readlines()
# print(lines)

# # 移除名字直到输入空格
# names = ["Ada", "Alan", "Bill", "John"]
# print(",".join(names))
# name_to_remove = input("Who do you want to remove? ").title()  # .title=视为标题，首字母大写
# while name_to_remove != "":
#     try:
#         names.remove(name_to_remove)
#     except ValueError:
#         print("Not in list!")
#     print(",".join(names))
#     name_to_remove = input("Who do you want to remove? ").title()
# print("Good bay!")

# data = [['derek', 7], ['xavier', 80], ['bob', 612], ['chantanelle', 9]]

# Output: [('name', 'Bob'), ('age', 99), ('day', 'Wed'), ('height', 1.75)]
# from operator import itemgetter
# name_to_number = {"Derek": 7, "Xavier": 80, "Bob": 612, "Chantanelle": 9}
#
# max_name_length = max(len(name) for name in name_to_number)
#
# for name, number in name_to_number.items():
#     print(f"{name:<{max_name_length}} - {number:>3}")
#
# for name, number in sorted(name_to_number.items(), key=itemgetter(1), reverse=True):
#     print(f"{name:<{max_name_length}} - {number:>3}")

# TEETH_INDEX = 1
# monsters = [["Mike", 340, "blue"],
# ["James", 14, "green"],
# ["Randall", 24, "purple"]]
# scary_monsters = [monster for monster in monsters if monster[TEETH_INDEX] > 16]
# print(scary_monsters)

# class Monster:
#     def __init__(self, name="Mike", number_of_teeth=0, colour="blue"):
#         self.name = name
#         self.number_of_teeth = number_of_teeth
#         self.colour = colour


# Define the Monster class (with is_scary method)

class User:

    def __init__(self, name):

        self.name = name
        self.tacos = 5
        self.score = 0

    def give_taco(self, other_user):

        if self.tacos > 0:
            self.tacos -= 1
            other_user.score += 1
        else:
            print(f"{self.name} has no tacos left to give!")

    def __str__(self):
       
        return f"{self.name}, {self.score} points, {self.tacos} tacos left"



