#Rafael Garcia
# April 11 2018
# This program prints a list of the worst driving offenders with attributes




#Import pandas for reading and analyzing CSV data:
import pandas as pd

csvFile = input('Enter CSV file name: ')         # Ask for the Name of the CSV file
sd = input('Enter attribute: ')
tickets = pd.read_csv(csvFile)     #Read in the file to a dataframe
print("The 10 worst offenders are:")
print(tickets[sd].value_counts()[:10]) #Print out the dataframe