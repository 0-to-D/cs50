import csv

students = []

with open("file.csv") as file:
    reader = csv.reader(file)
    for name, address in reader:
        students.append({"name": name, "address": address})

for each in sorted(students, key=lambda name : name['name']):
    print(f"name is {each['name']} and address is {each['address']}")
