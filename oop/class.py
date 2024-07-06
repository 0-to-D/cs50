class Student:
    def __init__(self, name, grade):
        if not name:
            raise ValueError("missing name")
        if grade not in ["A", "B", "C", "D", "F"]:
            raise ValueError("invalid grade")
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"name {self.name}\ngrade{self.grade}"

def main():
    student = get_data()
    print(f"name: {student.name}, grade: {student.grade}")

def get_data():
    #student = Student()
    name = input("give name ")
    grade = input("give grade")
    try:
        student = Student(name, grade)
    except ValueError:
        raise ValueError
    print(student)
    return student


if __name__ == "__main__":
    main()
