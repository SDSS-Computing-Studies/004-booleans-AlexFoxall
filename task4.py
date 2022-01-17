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
input_string = input('enter a sentence')
family_list  = input_string.split(" ")
for name in family_list:
    if name == "password":
        print('the sentence contains password')
    else:
        print('the sentence does not contain password')