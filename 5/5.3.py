import os


def counter(path):
    count = 0
    for filename in os.listdir(path):
        newpath = os.path.join(path, filename)
        if  os.path.isdir(newpath):
            count += counter(newpath)
        else:
            count += 1
    return count

print(counter('.'))