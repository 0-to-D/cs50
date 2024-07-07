students = [
    {"name": "harry", "house":"gryffendor"},
    {"name":"hermoine", "house":"gryffendor"},
    {"name":"draco", "house":"slytherin"},
]


gryffendors = [
    each["name"] for each in students if each["house"] == "gryffendor"
]

for gryffendor in gryffendors:
    print(gryffendor)
