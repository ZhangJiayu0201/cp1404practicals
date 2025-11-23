
from unreliable_car import UnreliableCar


def main():
    """Test unreliable_car class."""

    drive_distance = 10
    test_times = 10

    first_car = UnreliableCar("First car", 100, 80)
    second_car = UnreliableCar("Second car", 100, 20)

    for t in range(1, test_times + 1):
        print(f"\nNumber of attempts{t}:")
        print(f"{first_car.name} drive {first_car.drive(drive_distance)} km")
        print(f"{second_car.name} drive {second_car.drive(drive_distance)} km")

    print("\nFinal states:")
    print(first_car)
    print(second_car)


if __name__ == "__main__":
    main()
