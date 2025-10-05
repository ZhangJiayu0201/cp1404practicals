# Q1.
infile = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=infile)
infile.close()


# Q2.
infile = open("name.txt", "r")
name = infile.read()
print(f"Hi {name.strip()}!")
infile.close()


# Q3.
with open("number.txt", "r") as file:
    line1 = int(file.readline())
    line2 = int(file.readline())
    print(line1 + line2)


# Q4.
total = 0
with open("number.txt", "r") as file:
    for line in file:
        total += int(line)
print(total)

