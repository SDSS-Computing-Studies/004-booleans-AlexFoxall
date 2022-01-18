#! python3

"""
Have the user enter in a sentence. 
Check to see if the word "password" is located in the sentence

Inputs:
a sentence

Outputs:
"the sentence contains password"
"the sentence does not contain password"

Examples:
Enter a sentence: I will not buy this record, it is scratched.
the sentence does not contain password

Enter a sentence: The best password is no password.
the sentence contains password
"""
def mc():
    e= False
    input_string = input('enter a sentence')
    x = input_string.split(" ")
    for i in x:
       if i == "password":
           e = True
           print('the sentence contains password')
       if e == True:
           break
    return e

if mc() == False:
    print("the sentence does not contain password")
