def howalp(alp):
    if alp <= 'N':
        return ord(alp) - ord('A')
    else:
        return ord('Z') - ord(alp) + 1

def solution(name):
    answer = 0
    p = 0
    alplist = []
    for i in name:
        alplist.append(howalp(i))

    answer += alplist[0]
    alplist[0] = 0

    while any(alplist):
        pu, pd = 1, 1
        while alplist[(p + pu) % len(alplist)] == 0:
            pu += 1
        while alplist[p - pd] == 0:
            pd += 1

        if pu <= pd:
            answer += alplist[(p + pu) % len(alplist)] + pu
            alplist[(p + pu) % len(alplist)] = 0
            p = (p + pu) % len(alplist)
        else:
            answer += alplist[p - pd] + pd
            alplist[p - pd] = 0
            p = (p - pd + len(alplist)) % len(alplist)

    return answer

print(solution("CAACCBBBSBBN"))
#O  P  Q  R S T U V W X Y Z A B C D E F G H I J K  L  M  N
#12 11 10 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 10 11 12 13