def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for num in numbers:
        num = int(num)
        if num == 1 or num == 4 or num == 7:
            left = num
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:
            right = num
            answer += 'R'
        else:
            if num == 0:
                num = 11
            nn = divmod(num - 1, 3)

            ln = divmod(left - 1, 3)
            lnn = 0

            if ln[0] <= nn[0]:
                lnn += nn[0] - ln[0]
            else:
                lnn += ln[0] - nn[0]

            if ln[1] <= nn[1]:
                lnn += nn[1] - ln[1]
            else:
                lnn += ln[1] - nn[1]

            rn = divmod(right - 1, 3)
            rnn = 0

            if rn[0] <= nn[0]:
                rnn += nn[0] - rn[0]
            else:
                rnn += rn[0] - nn[0]

            if rn[1] <= nn[1]:
                rnn += nn[1] - rn[1]
            else:
                rnn += rn[1] - nn[1]

            print(ln, nn, rn)
            print(left, num, right,  lnn, rnn)

            if lnn > rnn:
                right = num
                answer += 'R'
            elif lnn < rnn:
                left = num
                answer += 'L'
            else:
                if hand == 'right':
                    right = num
                    answer += 'R'
                else:
                    left = num
                    answer += 'L'


    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))