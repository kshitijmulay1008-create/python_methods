class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def car_details(self):
        return f"Brand: {self.brand}, Color: {self.color}, Wheels: {Car.wheels}"

    @classmethod
    def set_wheels(cls, number):
        cls.wheels = number

    @staticmethod
    def is_motor_vehicle():
        return True


car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print(car1.car_details())

Car.set_wheels(6)
print(car2.car_details())

print(Car.is_motor_vehicle())
