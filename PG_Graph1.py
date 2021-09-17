def solution(n, edge):
    answer = 0
    edge.sort()

    nodelist = [0]
    visitlist = [0] * n
    for i in range(n - 1):
        nodelist.append(99999999)

    print(edge)
    for i in edge:
        if nodelist[i[1] - 1] > nodelist[i[0] - 1] + 1:
            nodelist[i[1] - 1] = nodelist[i[0] - 1] + 1

        if nodelist[i[0] - 1] > nodelist[i[1] - 1] + 1:
            nodelist[i[0] - 1] = nodelist[i[1] - 1] + 1

        print(nodelist)

    for i, v in enumerate(nodelist):
        if v == 99999999:
            nodelist[i] = 0
    print(nodelist)

    m = max(nodelist)
    for i in nodelist:
        if i == m and i != 0:
            answer += 1

    return answer

print(solution(6, [[1,2],[3,4],[4,5],[2,6] ,[6,5]]))