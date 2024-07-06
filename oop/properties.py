class Students:

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} {self.house}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["a", "b", "c"]:
            raise ValueError("error aahe bala line 17 la")
        else:
            self._house = house


def main():
    student = student_constructor()
    print(student)
    print(type(student))
    #student.house = "yoyo"


def student_constructor():
    name = input("enter name: ")
    house = input("enter house ")
    return Students(name, house)

if __name__ == "__main__":
    main()


