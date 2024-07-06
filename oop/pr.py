class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} {self.house}"

    @property
    def name(self):
        return self._kome

    @name.setter
    def name(self, name):
        if name not in ["a","b","c","d","e"]:
            raise ValueError
        self._kome = name


def student_constructor():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house)

def main():
    student1 = student_constructor()
    print(student1)

if __name__ == "__main__":
    main()
