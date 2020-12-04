#!/usr/bin/env python3

with open("input.txt") as f:
  input = [x for x in f]

passport = []
valid = 0
for i in range(len(input)):
    input[i] = input[i].split()
    try:
        input[i][0] 
        for j in range(len(input[i])):
            input[i][j] = input[i][j].split(":")
            passport.append(input[i][j])
    except:
            count = 0
            for i in range(len(passport)):
                if 'ecl' in passport[i]:
                    if 'amb' in passport[i] or 'blu' in passport[i] or 'brn' in passport[i] or 'gry' in passport[i] or 'grn' in passport[i] or 'hzl' in passport[i] or 'oth' in passport[i]:
                        count = count + 1
                if 'pid' in passport[i]:
                    if len(passport[i][1]) == 9 and passport[i][1].isdigit():
                        count = count + 1

                if 'eyr' in passport[i]:
                        if len(passport[i][1]) == 4 and passport[i][1].isdigit() and int(passport[i][1]) >= 2020 and int(passport[i][1]) <= 2030:
                            count = count + 1

                #a # followed by exactly six characters 0-9 or a-f.
                if 'hcl' in passport[i]:
                    if passport[i][1][0] == '#' and len(passport[i][1]) == 7:
                        is_good = True
                        for j in range(len(passport[i][1])):
                            if passport[i][1][j].isalpha():
                                if ord(passport[i][1][j]) <= 97 and ord(passport[i][1][j]) >= 103:
                                    is_good = False
                        
                        if is_good:
                            count = count + 1


                if 'byr' in passport[i]:
                    if passport[i][1].isdigit() and len(passport[i][1]) == 4 and int(passport[i][1]) >= 1920 and int(passport[i][1]) <= 2002:
                        count = count + 1

                if 'iyr' in passport[i]:
                    if passport[i][1].isdigit() and len(passport[i][1]) == 4 and int(passport[i][1]) >= 2010 and int(passport[i][1]) <= 2020:
                        count = count + 1

                if 'hgt' in passport[i]:
                    is_good = True
                    for j in range(1,len(passport[i][1]) - 2):
                        if passport[i][1][j].isalpha():
                            is_good = False
                            
                    last_2 = passport[i][1][len(passport[i][1])-2:]
                    if last_2 != "in" and last_2 != "cm":
                        is_good = False
                    if last_2 == "cm":
                        if int(passport[i][1][:-2]) < 150 or int(passport[i][1][:-2]) > 193:
                            is_good = False

                    elif last_2 == "in":
                        if int(passport[i][1][:-2]) < 59 or int(passport[i][1][:-2]) > 76:
                            is_good = False
                        

                    if is_good:
                        count = count + 1

            print(count)
            if count == 7:
                valid = valid + 1
                print(passport)

            passport = []
print(valid)