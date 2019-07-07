"""
OOP example
"""
class Engine:
    works = False

class Car:
    acceleration = 10

    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.in_motion = False
        self.speed = 0
        self._engine = Engine()

    def print_reg_number_and_speed(self):
        print(f'{self.registration_number} - {self.speed}km/h')

    def drive(self):
        self.in_motion = True
        self.foo = 2

    def accelerate(self):
        self.speed += self.acceleration

    def stop(self):
        self.in_motion = False
        self.speed = 0

    def __start_engine(self):
        self._engine.works = True

    def engine_status(self):
        return self._engine.works

    def start(self):
        self._start_engine()

if __name__ == "__main__":
    opel_astra = Car('ELC0001')
    print(opel_astra.engine_status())
    opel_astra.__start_engine()
    print()
    print(opel_astra.engine_status())