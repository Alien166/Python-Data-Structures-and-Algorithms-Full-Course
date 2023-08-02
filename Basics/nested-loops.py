rows = int(input("Enter number of rows"))
columns = int(input("Enter number of columns"))
symbol = input("Enter number of symbol to use")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()
