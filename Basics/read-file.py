try:
    with open('text.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("File Not Found")
