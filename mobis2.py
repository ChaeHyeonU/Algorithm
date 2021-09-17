def solution(a):
    answer = []
    for i in a:
        if i.count('b') % 2 == 1 or i.count('a') < 1:
            answer.append(False)
            continue
        if i.count('a') == len(i):
            answer.append(True)
            continue

        while len(i) > 1:

            if i[0] == 'b' and i[-1] == 'b':
                i = i.strip('b')
            else:
                i = i.strip('a')
            if i.count('a') == len(i):
                break
            if i.count('b') ==

        if i.count('a') == len(i) and len(i) != 0:
            answer.append(True)
        else:
            answer.append(False)

    return answer

print(solution(["aaaa","bbaa","bababa","bbbabababbbaa"]))