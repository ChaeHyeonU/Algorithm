import math
import re


def csplit(sep_list, str_to):
    reg_exp = '|'.join(map(re.escape, sep_list))
    return re.split(reg_exp, str_to)


def solution(dartResult):
    answer = 0
    sp1 = "10", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    sp2 = "S", "D", "T", "*", "#"
    num = csplit(sp2, dartResult)
    opt = csplit(sp1, dartResult)
    while '' in num:
        num.remove('')
    while '' in opt:
        opt.remove('')
    for i,v in enumerate(num):
        num[i] = int(v)

    for i, v in enumerate(opt):

        if v[0] == 'D':
            num[i] = math.pow(num[i], 2)

        if v[0] == 'T':
            num[i] = math.pow(num[i], 3)

        if len(v) == 2:
            if v[1] == '*':
                if i > 0:
                    num[i - 1] = num[i - 1] * 2
                num[i] = num[i] * 2
            elif v[1] == '#':
                num[i] = num[i] * -1

    for i in num:
        answer += i
    return int(answer)

print(solution("1S2D*3T"))