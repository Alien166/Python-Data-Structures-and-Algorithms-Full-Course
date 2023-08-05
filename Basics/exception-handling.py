try:
    num = int(input("Enter the first number"))
    dom = int(input("enter the second number"))
    result = num / dom

except ZeroDivisionError as e:
    print(e)
    print('you can;t divide by zero')
except ValueError as e :
    print(e)
    print('plz enter a number')

except Exception as e :
    print(e)
    print("u have a something wrong")

else:
    print(result)

finally:
    print("this will always excute")
