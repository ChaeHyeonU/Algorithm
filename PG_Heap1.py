import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)

    while 1:
        if len(scoville) <= 1 and scoville[0] < K:
            count = -1
            break
        if scoville[0] >= K:
            break
        new = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new)
        count += 1

    return count

