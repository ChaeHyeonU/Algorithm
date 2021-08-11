import sys

INF = sys.maxsize
N, M = map(int, input().split())
G = [[INF] * N for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    G[x-1][y-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if G[i][k] + G[k][j] == 2:
                G[i][j] = 1


cnt = [0]*N

for i in range(N):
    for j in range(N):
        if G[i][j] == 1:
            cnt[i] += 1
            cnt[j] += 1

print(cnt.count(N-1))