def enter_garage(garage, car_id, entry_hour):
    if car_id in garage["cars"]:
        raise ValueError

    if len(garage["cars"]) >= garage["capacity"]:
        raise ValueError
    garage["cars"][car_id] = entry_hour


def exit_garage(garage, car_id):
    if car_id not in garage["cars"]:
        raise KeyError
    del garage["cars"][car_id]

def get_available_spots(garage):
    spots = garage["capacity"] - len(garage["cars"])
    if spots <0:
        return 0 
    return spots



def calculate_fee(hours, rate):
    return 100