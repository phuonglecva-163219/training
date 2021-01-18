import re
import sys
input = '123456789'
listToken = ['+', '-', '']
lis = [''] * 8  

def lietKe100(i, lis=lis):
    for j in listToken:
        lis[i] = j
        if i == 7:
            # print(lis)
            s = ''
            for k in range(len(input) - 1):
                s += input[k] + lis[k]
            s += input[-1]
            if eval(s) == 100:
                print(s +' = ' + str(eval(s)))
                break
            lis = [''] * 8
        else:
            lietKe100(i + 1)

lietKe100(0)