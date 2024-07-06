class Student:
    def __init__(self, name, house, pat):

        if not name:
            raise ValueError("enter the name")
        if house not in ["a", "b", "c", "d", "e"]: 
            raise ValueError("invalid house")
        if not pat:
            raise ValueError("enter the pat")

        self.name = name
        self.house = house
        self.pat = pat

    def __str__(self):
        return f"{self.name} {self.house} {self.pat}"

    def charm(self):
        match self.pat:
            case "smile":
                return "😂"
            case "dog":
                return "🐒"
            case "heart":
                return "🫀"
            case _:
                return "🔥"



def main():
    student1 = get_student()
    student2 = get_student()
    print(student1, student2)
    print(student1.charm())
    print(student2.charm())

def get_student():
    name = input("enter name:  ")
    house = input("enter house:  ")
    pat = input("enter patronus:  ")
    return Student(name, house, pat)

if __name__ == "__main__":
    main()
