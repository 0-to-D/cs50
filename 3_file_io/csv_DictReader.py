import csv

students = []

with open("file2.csv") as file:
    reader = csv.DictReader(file)
    for  each in reader:
        students.append({"name":each["name"], "address":each["address"]})

for each in students:
    #    print(f"name:{each['name']} addeess:{each['address']}")
    print(f"name is {each['name']} and address is {each['address']}")
