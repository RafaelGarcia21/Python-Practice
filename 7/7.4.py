def goalSeek(function, lowLimit, highLimit, target, maxError=.01):
    error = maxError + 1

    while error > maxError:
        guess = (lowLimit + highLimit) / 2
        print('lo={0} hi={1}'.format(lowLimit, highLimit))
        result = function(guess)
        print('guess={0} result={1}'.format(guess, result))
        error = abs(result - target)
        print('error={0}'.format(error))
        if result > target:
            highLimit = guess
        if result < target:
            lowLimit = guess
        print('lo={0} hi={1}'.format(lowLimit, highLimit))
        input('Enter to continue\n\n')

    return guess


def mystery(x):
    return x * x - 10 * x + 25


print(goalSeek(mystery, 0, 5, 10, .001))
