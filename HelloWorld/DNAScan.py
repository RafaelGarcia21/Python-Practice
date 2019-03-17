#Rafael Garcia
#Date Feb 16 2018
# This program prints the out sequence is as well as GC-content


dna = input("Enter DNA string: ")
d = len(dna)
print("Length is ",d)

num1 = dna.count('C')
num2 = dna.count('G')


gc = (num1 + num2) / d

#dnaP = gc * 100
#print(gc)
print("GC-content is " , gc)