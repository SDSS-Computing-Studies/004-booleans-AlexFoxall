#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
import math
x = input("enter first side length")
y = input("enter second side length")
n = input("enter third side length")

list1 = [x,y,n]
list1 = sorted(list1)
j = (list1[2])
k = (list1[1])
l = (list1[0])

j = int(j)
k = int(k)
l = int(k)

d = k ** 2  
r = l ** 2
d = r + d
v = j ** 2
if d == v:
    print("that is a right angle triangle")
else:
    print("that is an obtuse triangle")