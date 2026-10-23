class car:
    def __init__(self):
        self.clutch = False
        self.brake = True
        self.acc = False

    def start(self):
        self.clutch = True
        self.brake = False
        self.acc = True
        print("Car Started")

c1 = car()
c1.start()