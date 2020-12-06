#!/usr/bin/env python3


def count_answers(ans):
    count = 0
    dec_form = []
    group = [""]
    for i in range(len(ans)):
        if ans[i][0] == '\n':
            dec_form.append(dict.fromkeys(group[0]))
            print(dec_form[len(dec_form)-1])
            count = count + len(dec_form[len(dec_form)-1])
            group = [""]

        else:
            group[0] = group[0]+ans[i].strip('\n')
    print(count)

def count_answers_everyone(ans):
    count = 0
    dec_form = []
    group = [""]
    it = 0
    for i in range(len(ans)):
        if ans[i][0] == '\n':
            for j in range(len(group[0])):
                print(group[0])
                try:
                    if group[0].count(group[0][0]) == it:
                        dec_form.append(group[0][0])
                        count = count + 1
                except:
                    print("")
                try:
                    group[0] = group[0].strip(group[0][0])
                except:
                    print("")
                # print(group[0])
            group = [""]
            it = 0

        else:
            group[0] = group[0]+ans[i].strip('\n')
            it = it + 1
    print(count)
    



if __name__ == "__main__":


  with open("input.txt") as f:
    input = [x for x in f]
  
  count_answers_everyone(input)