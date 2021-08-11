def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    l1 = len(p1)
    l2 = len(p2)
    l3 = len(p3)

    an = [0,0,0]

    for i in range(len(answers)):
        if answers[i] == p1[i % l1]:
            an[0] += 1
        if answers[i] == p2[i % l2]:
            an[1] += 1
        if answers[i] == p3[i % l3]:
            an[2] += 1

    for i, ans in enumerate(an):
        if ans == max(an):
            answer.append(i+1)

    return answer
