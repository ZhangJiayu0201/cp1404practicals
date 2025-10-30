"""
Emails
Estimate: 30 minutes
Actual:   25 minutes
"""

email_to_name = {}

email = input("Email: ").strip()
while email != "":
    name_in_email = email.split("@")[0]
    name = name_in_email.split(".")
    uncheck_name = " ".join(name).title()
    name_check = input(f"Is your name {uncheck_name}? (Y/n) ").strip()
    if name_check == "" or name_check.lower() == "y":
        real_name = uncheck_name
    else:
        real_name = input("Name: ").strip()
    email_to_name[email] = real_name
    email = input("Email: ").strip()
for email, real_name in email_to_name.items():
    print(f"{real_name} ({email})")
