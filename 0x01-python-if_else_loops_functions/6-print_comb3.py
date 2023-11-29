#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x + 1, 10):
        if x == 5 and y == 8:
            print('58')
        else:
            print('{}{},'.format(x, y), end='')
