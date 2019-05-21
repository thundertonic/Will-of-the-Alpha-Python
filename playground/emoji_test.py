import random

for i in range(12):
    string = ''
    for j in range (12):
        if random.uniform(0, 1) < 0.1:
            string += '🐠'
        elif random.uniform(0, 1) < 0.1:
            string += '⛰'
        else:
            string += '🌊'
    print(string)