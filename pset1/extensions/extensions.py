userInput = input("File name: ").strip().lower()

if userInput.endswith(".gif"):
    print("image/gif")
elif userInput.endswith(".jpg") or userInput.endswith(".jpeg"):
    print("image/jpeg")
elif userInput.endswith(".png"):
    print("image/png")
elif userInput.endswith(".pdf"):
    print("application/pdf")
elif userInput.endswith(".txt"):
    print("text/plain")
elif userInput.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")