import heapq
def solution(jobs):
    answer = 0
    time = 0
    timebefore = -1
    hq = []
    n = len(jobs)
    nn = n
    while nn > 0:
        for job in jobs:
            if timebefore < job[0] <= time:
                heapq.heappush(hq, job[1])
                answer -= job[0]

        if len(hq) > 0:
            a = heapq.heappop(hq)
            timebefore = time
            time += a
            answer += time
            nn -= 1
        else:
            time += 1

    return answer // n

print(solution([[0, 3], [1, 9], [2, 6]]))