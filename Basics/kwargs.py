def hello(**kwargs):
    #print("hello" +kwargs['first'] + kwargs['middle'] +kwargs['last'])
    print("Hello" ,end=" ")
    for kay,value in kwargs.items():
        print(value,end="")


hello(first="abdeltawab",middle="mohamed",last="code")
