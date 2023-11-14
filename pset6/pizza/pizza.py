from sys import argv, exit
from tabulate import tabulate
import csv

if len(argv) != 2 or argv[1] and argv[1].endswith(".csv") == False:
    exit("You must provide a CSV file")

try:
    with open(argv[1]) as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    exit("File was not found")
