import random


A = []
numbers = range(1,10)
for i in numbers:
    A.append(random.randint(1,10))
print(set(A))


A = []
numbers = range(1,10)
for i in numbers:
    A.append(i)
    randomNumbers = random.choices(A,k=10)
print(A)
print(set(randomNumbers))

A = []
randomNumbers = []
numbers = range(1,10)
for i in numbers:
    A.append(i)
    x=1
    # while x < 3:
    #     x=x+1
    randomNumbers.append(random.choice(A))
print(set(randomNumbers))
 
