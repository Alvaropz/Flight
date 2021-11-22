import random
import codecs
import sys

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = {}

    def seats_distribution(self, rows):
        letters = ["A", "B", "C", "D", "F", "G"]
        for bussiness_class in range(1, rows+1):
            for letter_seat in range(0, 6):
                current_value = str(bussiness_class) + letters[letter_seat]
                self.seats[f"{current_value}"] = None
        return self.seats
    
    def populating_flight(self):
        while self.capacity:
            for seat in self.seats:
                if len(passengers) > 0:
                    random_assignation = random.randrange(0, len(passengers))
                    self.seats[seat] = passengers[random_assignation]
                    passengers.pop(random_assignation)
                self.capacity -= 1
        return self.seats

file_selected = sys.argv[1]
passengers = []
with codecs.open(file_selected, "r", encoding='utf8') as f:
    for name in f:
        passengers.append(name.rstrip("\r\n"))

aircraft_model = input("What aircraft will you use for this flight?: ")
if aircraft_model == "A320":
    rows = 30
    capacity = 30 * 6
if aircraft_model == "B777":
    rows = 63
    capacity = 63 * 6

flight = Flight(capacity)
if len(passengers) > capacity:
    print("There are more passengers than seats avaiable for this flight.")
else:
    print("There are enought seats for this flight. Populating this flight...")
    flight.seats_distribution(rows)
    final_dict = flight.populating_flight()
    for seat, passenger in final_dict.items():
        if passenger:
            print(f"The seat {seat} has been assigned to {passenger}.")
        else:
            break

        