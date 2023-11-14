from sys import argv, exit
from PIL import Image, ImageOps

if len(argv) < 3:
    exit("Too few command-line arguments")

if len(argv) > 3:
    exit("Too many command-line arguments")

if argv[1].endswith(".jpg") == False and argv[1].endswith(".jpeg") == False and argv[1].endswith(".png") == False:
    exit("Invalid input")

if argv[2].endswith(".jpg") == False and argv[2].endswith(".jpeg") == False and argv[2].endswith(".png") == False:
    exit("Invalid output")

file_1_ext = argv[1].split(".")[-1]
file_2_ext = argv[2].split(".")[-1]

if file_1_ext != file_2_ext:
    exit("Input and output have different extensions")

try:
    photo = Image.open(argv[1])
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size
    photo = ImageOps.fit(photo, shirt_size)
    photo.paste(shirt, shirt)
    photo.save(argv[2])

except FileNotFoundError:
    exit("Input does not exist")
