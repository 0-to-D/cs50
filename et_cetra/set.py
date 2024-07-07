students = [
    {"name": "hermoine", "house": "griffendor"},
    {"name": "potter", "house": "griffendor"},
    {"name": "draco", "house": "slytherin"}
]

houses = set()
for student in students:
    if student["house"] not in houses:
        houses.add(student["house"])

for each in sorted(houses):
    print(each)
