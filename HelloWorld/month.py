# CSci 127 Teaching Staff
# October 2017
# A program that uses functions to print out months.
# Modified by:  Rafael Garcia

def monthString(monthNum):
    """
    Takes as input a number, monthNum, and
    returns the corresponding month name as a string.
    Example: monthString(1) returns "January".
    Assumes that input is an integer ranging from 1 to 12
    """

    monthString = ""

    if monthNum == "1":
        monthString == 'January'
    elif monthNum == "2":
        monthString == 'February'
    elif monthNum == "3":
        monthString == 'March'
    elif monthNum == "4":
        monthString == 'April'
    return(monthString)


def main():
    n = int(input('Enter the number of the month: '))
    mString = monthString(n)
    print('The month is', mString)


# Allow script to be run directly:
if __name__ == "__main__":
    main()
