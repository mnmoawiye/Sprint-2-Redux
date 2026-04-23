from garage import enter_garage

def test_enter_garage():
    garage = {"capacity": 2, "cars": {}}
    enter_garage(garage, "A", 5)
    assert garage["cars"]["A"] == 5