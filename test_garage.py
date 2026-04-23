from garage import enter_garage

def test_enter_garage():
    garage = {"capacity": 2, "cars": {}}
    enter_garage(g, "A", 5)
    assert g["cars"]["A"] == 5