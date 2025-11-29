
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's drive!")

    taxis = [Taxi("Prius", 100),SilverServiceTaxi("Limo", 100, 2),SilverServiceTaxi("Hummer", 200, 4)]

    total_bill = 0.0
    current_taxi = ""
    menu = "q)uit, c)hoose taxi, d)rive"

    print(menu)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            index = 0

            for taxi in taxis:
                print(f"{index} - {taxi}")
                index = index + 1
            taxi_choice = input("Choose taxi: ")

            if taxi_choice.isdigit():
                taxi_choice = int(taxi_choice)
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            else:
                print("Invalid input (not a number).")

        elif choice == "d":
            distance = int(input("Drive how far? "))
            current_taxi.drive(distance)
            trip_cost = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            total_bill += trip_cost

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(menu)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
