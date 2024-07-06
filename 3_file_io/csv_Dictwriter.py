import csv

name = input("enter name   ")
address = input("enter address  ")

with open("file2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","address"])
    writer.writerow({"name":name,"address":address})
