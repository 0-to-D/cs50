import csv

name = input("whats name  ")
address = input("whats address  ")

with open("file2.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name,address])
