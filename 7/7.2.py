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

def makePower(exp):
    def power(number):
        return number**exp
    return power

for exp in range(2,11):
    power = makePower(exp)
    print(exp, goalSeek(power, 0, 5, 2))