from garage import enter_garage, get_available_spots

def test_enter_garage():
    garage = {"capacity": 2, "cars": {}}
    enter_garage(garage, "A", 5)
    assert garage["cars"]["A"] == 5

def test_available_spots_empty():
    garage = {"capacity": 10, "cars": {}}
    assert get_available_spots(garage) == 10
