import heapq
import sys
maxh = []
minh = []


N = int(sys.stdin.readline())
for _ in range(N):
    innum = int(sys.stdin.readline())
    if len(maxh) > len(minh):
        heapq.heappush(minh, innum)
    else:
        heapq.heappush(maxh, (-innum, innum))

    if maxh and minh:
        if maxh[0][1] > minh[0]:
            a = heapq.heappop(maxh)[1]
            b = heapq.heappop(minh)
            heapq.heappush(minh, a)
            heapq.heappush(maxh, (-b, b))
    print(maxh[0][1])