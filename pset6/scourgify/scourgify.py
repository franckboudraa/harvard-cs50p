from sys import argv, exit
import csv

if len(argv) != 3:
    exit("You must provide two arguments")

if argv[1].endswith(".csv") == False:
    exit("You must provide a valid CSV file")

if argv[2].endswith(".csv") == False:
    exit("You must provide a valid CSV file")


students = []

try:
    with open(argv[1]) as file:
        reader = csv.DictReader(file)

        for row in reader:
            last, first = row["name"].split(",")
            students.append({"first": first.strip(), "last": last.strip(), "house": row["house"].strip()})
except:
    exit("Could not read input file")

with open(argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

    writer.writeheader()

    for student in students:
        writer.writerow(student)
