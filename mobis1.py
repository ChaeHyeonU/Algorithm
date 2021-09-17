def solution(dice):
    answer = 0

    aa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    newl = []
    for di in dice:
        newl.append(list(set(di)))
    for nn in newl:

    a1 = aa - newl[0]
    print(a1, 1)


    return newl

print(solution([[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]))

#  1 2 3 4 5 6 :: 0 1 7 8 9
#  0 7 8 9  ::  2 3 4 5 6


#  4 6 7 8  ::  3 5 6 9  ::  0 1 2 8 9