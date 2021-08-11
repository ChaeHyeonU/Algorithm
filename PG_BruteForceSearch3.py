def solution(brown, yellow):
    answer = []

    nb = (brown - 4) // 2
    for i in range(1, nb):
        if i * (nb - i) == yellow:
            answer.append(nb - i + 2)
            answer.append(i + 2)
            break;

    return answer

print(solution(24,24))