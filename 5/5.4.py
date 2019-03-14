import my

def alphabetize(s):
    letters = list(s)
    letters.sort()
    return my.rejoin(letters)

unscramble = {}

with open('pap.txt') as book:
    for line in book:
        for word in my.cleanedup(line).split():
            key = alphabetize(word)
            if key in unscramble:
                if word not in unscramble[key]:
                    unscramble[key].append(word)
            else:
                unscramble[key] = [word]

puzzle = input('Puzzle: ')
key = alphabetize(puzzle)
if key in unscramble:
    print(unscramble[key])
else:
    print('No answer found')