def printFred(times):
    print('Fred')
    if times-1 > 0:
        printFred(times-1)

printFred(100)
