import heapq

def solution(operations):
    answer = []
    hq = []
    for ops in operations:
        op = ops.split(' ')
        if op[0] == "I":
            heapq.heappush(hq, int(op[1]))
        if op[0] == "D" and len(hq) != 0:
            if op[1] == "-1":
                heapq.heappop(hq)
            else:
                maxnum = heapq.nlargest(1, hq)[0]
                hq.remove(maxnum)

    if len(hq) == 0:
        answer = [0,0]
    else:
        answer.append(heapq.nlargest(1, hq)[0])
        answer.append(hq[0])


    return answer
