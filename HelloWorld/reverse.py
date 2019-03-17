#Name: Rafael Garcia
#Date: Feb 16 2018
#This program prints: prompts the user to enter a word and then prints out the word with each letter shifted right by 2



greet = input("Enter something usefull like a word: ")
newGreet = ""
for character in greet:
    o = ord(character) - ord('a') + 2
    wrap = o % 26
    PM = chr(ord('a') + wrap)
    newGreet = newGreet+ PM

print("Your word in code is \n", newGreet)