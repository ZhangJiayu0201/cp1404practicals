MINIMUM_LENGTH = 5
password = input("Enter password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"The length of your password must greater than {MINIMUM_LENGTH}!")
    password = input("Enter password: ")
print("*"*len(password))