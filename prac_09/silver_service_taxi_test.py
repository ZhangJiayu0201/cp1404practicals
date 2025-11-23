from silver_service_taxi import SilverServiceTaxi


def test_flagfall():
    """Test for flagfall is always charged."""
    taxi = SilverServiceTaxi("Test Taxi", 100, 1.0)
    fare = taxi.get_fare()
    assert fare == 4.50, f"Expected $4.50 flagfall, got ${fare}"


def test_fanciness():
    """Test fanciness affects."""
    taxi = SilverServiceTaxi("Test Taxi", 100, 4.0)
    expected_price = 1.23 * 4.0
    assert taxi.price_per_km == expected_price, f"Expected ${expected_price}/km, got ${taxi.price_per_km}/km"


    test_flagfall()
    test_fanciness()