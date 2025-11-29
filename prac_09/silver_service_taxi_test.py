from silver_service_taxi import SilverServiceTaxi


def test_example():
    """Test example."""
    drive_distance = 18
    fanciness = 2
    taxi = SilverServiceTaxi("Example Taxi", 100, fanciness)
    flagfall = taxi.flagfall
    price_per_km = taxi.price_per_km
    taxi.drive(drive_distance)
    fare = taxi.get_fare()
    # assert round(fare, 2) == round(price_per_km * drive_distance + flagfall,2), f"Expected ${price_per_km * drive_distance + flagfall}, got ${fare}"
    assert round(fare, 1) == round(price_per_km * drive_distance + flagfall,1), f"Expected ${price_per_km * drive_distance + flagfall}, got ${fare}"
    print(f"For an {drive_distance} km trip in a SilverServiceTaxi with fanciness of {fanciness}, the fare should be {fare}")


def test_flagfall():
    """Test for flagfall is always charged."""

    taxi = SilverServiceTaxi("Test flagfall Taxi", 100, 1.0)
    fare = taxi.get_fare()
    assert round(fare, 2) == 4.50, f"Expected $4.50 flagfall, got ${fare}"


def test_fanciness():
    """Test fanciness affects."""
    taxi = SilverServiceTaxi("Test fanciness Taxi", 100, 4.0)
    expected_price = 1.23 * 4.0
    assert round(taxi.price_per_km, 2) == expected_price, f"Expected ${expected_price}/km, got ${taxi.price_per_km}/km"


test_example()
test_flagfall()
test_fanciness()