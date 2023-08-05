import random

x = random.randint(1,8)
print(x)

y = random.random()
print(y)
# --------------------------
myList = ['rock' ,'paper','scissors' ]
z = random.choice(myList)
print(z)

# ---------------------------

cards = [1,2,3,4,5,6,7,8,'J','Q','D','F','E']
random.shuffle(cards)
print(cards)

