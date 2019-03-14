import cards

def evaluate(hand):
    fvCounts = {}
    for card in hand:
        fv = cards.faceValueOf(card)
        if fv in fvCounts:
            fvCounts[fv] += 1
        else:
            fvCounts[fv] = 1

    justCounts = []
    for fv in fvCounts:
        justCounts.append(fvCounts[fv])
    justCounts.sort()
    if justCounts == [1, 1, 1, 2]:
        return 'one pair'
    if justCounts == [1, 2, 2]:
        return 'two pair'
    if justCounts == [1, 1, 3]:
        return 'three of a kind'
    if justCounts == [2,  3]:
        return 'full house'
    if justCounts == [1, 4]:
        return 'four of a kind'
    return 'nothing'


hand = cards.shuffledDeck()[:5]
print(hand)
print(evaluate(hand))