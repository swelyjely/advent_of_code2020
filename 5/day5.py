#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def find_my_seat(un_s):
  s = sorted(un_s,key=lambda k: [k[1],k[0]])
  output = [0,0]
  for i in range(len(s)-1):
    if (s[i+1][0] - s[i][0]) == 2:
      output[0] = s[i][0] + 1
      output[1] = s[i][1]

  return output
  
if __name__ == "__main__":

  with open("input.txt") as f:
    input = [x for x in f]
  
  seat_list_x = []
  seat_list_y = []
  combined_seats = []
  seat_id = []
  my_seat = []
  for i in range(len(input)):
    x = 0
    seats = [0,127]
    col = [0,7]
    seat_row = 0
    seat_col = 0
    for j in range(len(input[i][:-3])):
      ForB = input[i][j]
      diff = round((seats[1] - seats[0])/2)
      if ForB == 'F':
        seats[1] = seats[1]-diff
        if j == 6:
          seat_row = seats[0]
      elif ForB == 'B':
        seats[0] = seats[0] + diff
        if j == 6:
          seat_row = seats[1]
  
    for j in range(len(input[i][7:])):
      LorR = input[i][j+7]
      diff = round((col[1] - col[0])/2)
      if LorR == 'L':
        col[1] = col[1]-diff
        if j == 2:
          seat_col = col[0]
      elif LorR == 'R':
        col[0] = col[0] + diff
        if j == 2:
          seat_col = col[1]
    seat_id.append(seat_row * 8 + seat_col)
    combined_seats.append([seat_col,seat_row])
    seat_list_x.append(seat_col)
    seat_list_y.append(seat_row)

  my_seat = find_my_seat(combined_seats)
  print("my seat",my_seat)
    
  print(max(seat_id))
  plt.scatter(my_seat[0],my_seat[1],s=6)
  plt.scatter(seat_list_x,seat_list_y,s=6,marker='x',c='r')

  plt.show()
