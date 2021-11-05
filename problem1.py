#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# Hint: Use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"
import math
x = input("enter a number")
x = float(x)
x = x / 2
r = math.floor(x)
if x == r:
    print("this number is even")
else:
    print("this number is not even")