#!/usr/bin/python3
import random
number=random.randint(-10000,10000)
last_digits=abs(number) %10
print(f"Last  digits of {number} is {last_digits} and  less than 6 and  not 0") 
