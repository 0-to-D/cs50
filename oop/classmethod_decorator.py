import random

class Hat:
    houses = ["a", "b", "c"]

    def __init__(self, name, house):
        self.name = name
        self.house = house

    @classmethod
    def get(cls):
        name = input("enter name: ")
        house = input("enter house: ")
        return cls(name, house)

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(f"{name} is in {house}")

    
