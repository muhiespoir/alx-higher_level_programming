#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    rand_number = number % -10000
else:
    rand_number = number % 10000
print("Last digit of", number, "is", rand_number, end=' ')
if rand_number > 5:
    print("and is greater than 5")
elif rand_number == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
