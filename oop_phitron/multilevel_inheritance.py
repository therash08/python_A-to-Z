class vehicle:
    def __init__(self,name, price):
        self.name = name
        self.price = price

    def move(self):
        pass

class bus(vehicle):
    def __init__(self, name, price,seat):
        self.seat = seat
        super().__init__(name, price)

class truck(vehicle):
    def __init__(self, name, price,weight):
        self.weight = weight
        super().__init__(name, price)

class pickuptruck(truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)

class ACbus(bus):
    def __init__(self, name, price, seat,temperature):
        self.temperature = temperature
        super().__init__(name, price, seat)

    def __repr__(self):
        return super().__repr__()


green_line = ACbus('green', 50000,22,18)
print(green_line)