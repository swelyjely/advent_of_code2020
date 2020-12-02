#!/usr/bin/env python3


with open("numbers.txt") as f:
  numbers = [int(x) for x in f]

def pair():
    output = [(x,y) for x in numbers for y in numbers if x + y == 2020]
    return output[0][0]*output[0][1]

def trip():
    output = [(x,y,z) for x in numbers for y in numbers for z in numbers if x+y+z == 2020]
    return output[0][0]*output[0][1]*output[0][2]
print(pair())
print(trip())
