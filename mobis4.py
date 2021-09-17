def solution(p, q):
    answer = []
    for x in p:
        for y in q:
            x.sort()
            y.sort()


    return answer

print(solution([[4,3,3],[1,2,3],[3,2,4]], [[5,5],[5,1],[1,8]]))