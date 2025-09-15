class Car:
    # class variable
    brand = "Tesla"

    def __init__(self):
        self.speed = 0       # current speed
        self.gear = 0        # current gear
        self.engine_on = False

    # Method to start engine
    def engineStart(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"{Car.brand} engine started.")
        else:
            print("Engine is already running.")

    # Method to stop engine
    def engineStop(self):
        if self.engine_on:
            self.engine_on = False
            self.speed = 0
            self.gear = 0
            print(f"{Car.brand} engine stopped.")
        else:
            print("Engine is already off.")

    # Method to accelerate
    def accelerate(self):
        if self.engine_on:
            if self.speed < 300:
                self.speed += 25
                if self.speed > 300:
                    self.speed = 300
                print(f"Accelerated. Speed is now {self.speed} kmph.")
            if self.speed == 300:
                print("Max speed reached!")
        else:
            print("Start the engine first.")

    # Method for normal brake
    def brake(self):
        if self.engine_on:
            if self.speed > 0:
                self.speed -= 25
                if self.speed < 0:
                    self.speed = 0
                print(f"Brake applied. Speed is now {self.speed} kmph.")
            else:
                print("Car is already at rest.")
        else:
            print("Engine is off.")

    # Method for sudden brake
    def suddenBrake(self):
        if self.engine_on and self.speed > 0:
            self.speed = 0
            print("Sudden brake applied! Car stopped immediately.")
        else:
            print("Car is already at rest or engine is off.")

    # Method to change gear
    def gearChange(self):
        if self.engine_on:
            if self.gear < 5:
                self.gear += 1
                print(f"Gear changed. Current gear: {self.gear}")
            else:
                print("Already in maximum gear (5).")
        else:
            print("Start the engine first.")
