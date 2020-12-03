#!/usr/bin/env python3


with open("numbers.txt") as f:
  numbers = [x for x in f]

row_len = len(numbers[0]) - 1

def sled_ride_down(down):
    move_down = 0
    move_right = 0
    trees = 0
    while True:
        print(numbers[move_down][move_right])
        if numbers[move_down][move_right] == '#':
            trees = trees + 1
        move_down = move_down + down
        move_right = move_right + 1
        if move_right >= row_len:
            move_right = move_right - row_len 
        if move_down >= len(numbers):
            break
    return(trees)

def sled_ride_right(right):
    move_right = 0
    trees = 0
    for i in range(len(numbers)):
    
        if numbers[i][move_right] == '#':
            trees = trees + 1
        move_right = move_right + right
        if move_right >= row_len:
            move_right = move_right - row_len 
    return(trees)

print(sled_ride_down(2)*sled_ride_right(3)*sled_ride_right(5)*sled_ride_right(7)*sled_ride_right(1))
        