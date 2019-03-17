# Rafael Garcia
# April 30 2018
# This program  asks the user to enter a string. If the user enters an empty string,
# your program should continue prompting the user for a new string until they enter a non-empty string.
# Your program should then print out the string entered.


st = input('Enter a non-empty string: ')
while st == '':
    print('That was empty. Try again.')
    st = input('Enter a non-empty string: ')
print('You entered:', st)
