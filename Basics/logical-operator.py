temp =int(input("enter u temp"))

if temp >= 0 and temp <= 30:
    print("it's good")
elif temp > 0 or temp < 30:
    print("it's bad today")

    
if not(temp <= 30 and temp >= 0):
    print("it's nice")
