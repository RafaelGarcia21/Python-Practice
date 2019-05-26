def goalSeek(function, lowLimit, highLimit, target, maxError=.01):

    error = maxError + 1

    while error > maxError:
        guess = (lowLimit + highLimit) / 2
        result = function(guess)
        error = abs(result - target)
        if result > target:
            highLimit = guess
        if result < target:
            lowLimit = guess

    return guess


def square(number):
    return number * number


print(goalSeek(square, 0, 3, 2))
