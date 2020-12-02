#!/usr/bin/env python3


with open("numbers.txt") as f:
  numbers = [x for x in f]

def get_stuff(i):
        low = numbers[i].split('-')
        high = low[1].split()
        imp = high[2]
        letter = high[1][0]

        low = int(low[0])
        high = int(high[0])
        x = [low,high,imp,letter]
        return x

def part1():
    good = 0
    for i in range(len(numbers)):
        stuff = get_stuff(i)
        count = 0
        for j in range(len(stuff[2])):
            if stuff[2][j] == stuff[3]:
                count = count + 1
                
        if count >= stuff[0] and count <= stuff[1]:
            good = good + 1

    print("good:",good)

def part2():
    good = 0
    for i in range(len(numbers)):
        stuff = get_stuff(i)
        count = 0
        if (stuff[2][stuff[0]-1] == stuff[3] and not stuff[2][stuff[1]-1] == stuff[3]) or (not stuff[2][stuff[0]-1] == stuff[3] and stuff[2][stuff[1]-1] == stuff[3]):
            good = good + 1


    print("good:",good)


part1()
part2()