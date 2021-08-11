def solution(array, commands):
    answer = []
    for v in commands:
        tmp = array[v[0]-1:v[1]]
        tmp.sort()
        answer.append(tmp[v[2]-1])

    return answer