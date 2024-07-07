students = [
    {"name": "harry", "house":"gryffendor"},
    {"name":"hermoine", "house":"gryffendor"},
    {"name":"draco", "house":"slytherin"},
]

def is_gryffendor(s):
    return s["house"] == "gryffendor"

gryffendors1 = filter(is_gryffendor, students)

for gryffendor in gryffendors1:
    print(gryffendor["name"])








gryffendors2 = [
    each["name"] for each in students if each["house"] == "gryffendor"
]

for gryffendor in gryffendors2:
    print(gryffendor)
