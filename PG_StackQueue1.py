def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        count = 0
        while len(progresses) != 0 and progresses[0] >= 100:
            progresses.pop(0)
            count += 1

        if count != 0:
            answer.append(count)
    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
