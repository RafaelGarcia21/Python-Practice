pat4d = '{0:4d}'
pat2d = '{0:2d}'

print('   ', end = ' ')
for col in range(1, 11):
    print(pat4d.format(col), end='')
print()
print()

for row in range(1, 11):
    print(pat2d.format(row), end='')
    for col in range(1, 11):
        print(pat4d.format(row*col), end='')
    print()