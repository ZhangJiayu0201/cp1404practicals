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


name_list = ["Asda", "Basd", "Casd", "Dasd"]
# write code that creates files from a list of strings.
# Each file named with the value of the string. Write the string to the file.
for i in range(len(name_list)):
    with open(f"{name_list[i]}.txt", "w") as out_file:
        print(f"{i+1} {name_list[i]}", file=out_file)

# for name in name_list:
#     filename = name + ".txt"
#     with open(filename, "w") as file:
#         file.write(name)

# with open("A.txt", "r") as in_file:
#     lines = in_file.readlines()
# print(lines)
