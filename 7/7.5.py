entries = []

with open('phoneData.txt') as data:
    for line in data:
        items = line.split('\t')
        name = items[0] + ', ' + items[1]
        area = items[2][:3]
        number = items[2][4:-1]
        entries.append([name, area, number])

entries.sort()
for entry in entries:
    print('{0:24s}({1}) {2}'.format(entry[0], entry[1], entry[2]))
