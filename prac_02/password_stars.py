MINIMUM_LENGTH = 5


def main():
    password = get_password()
    method_name(password)


def method_name(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"The length of your password must greater than {MINIMUM_LENGTH}!")
        password = input("Enter password: ")
    return password


main()
