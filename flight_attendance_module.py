class attendance():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = attendance(3)

people = ["Harry", "ron", "Hermione", "Ginny", "Chris"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to fleight succesfully")
    else:
        print(f"Couldn't add {person} to flight due to no available sit")
