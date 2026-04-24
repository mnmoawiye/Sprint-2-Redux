import pytest
from garage import enter_garage, get_available_spots, exit_garage

def test_enter_garage():
    garage = {"capacity": 2, "cars": {}}
    enter_garage(garage, "A", 5)
    assert garage["cars"]["A"] == 5


def test_enter_full_garage():
    garage = {"capacity": 1, "cars": {"A": 1}}
    with pytest.raises(ValueError):
        enter_garage(garage, "B",2)

def test_enter_same_car_id():
    garage = {"capacity": 2, "cars": {"A": 1}}
    with pytest.raises(ValueError):
        enter_garage(garage, "A", 5)

def test_available_spots_empty():
    garage = {"capacity": 10, "cars": {}}
    assert get_available_spots(garage) == 10

def test_available_spots_full():
    garage = {"capacity": 2, "cars": {"A": 1, "B": 2}}
    assert get_available_spots(garage) == 0

def test_available_spots_partial():
    garage = {"capacity": 3, "cars": {"A": 1}}
    assert get_available_spots(garage) == 2


def test_exit_removes_car():
    garage = {"capacity": 2, "cars": {"A": 1}}
    exit_garage(garage, "A")
    assert "A" not in garage["cars"]

def test_exit_missing_car():
    garage = {"capacity": 2, "cars": {}}
    with pytest.raises (KeyError):
        exit_garage(garage,"A")

