import itertools
def solution(numbers):
    answer = 0
    a = set()
    for i in range(len(numbers)):
        a |= set(map(int, map("".join, itertools.permutations(list(numbers), i+1))))

    a -= set(range(0,2))

    for num in a:
        if num > 1:
            check = 0
            for i in range(2, (num // 2) + 1):
                if num % i == 0:
                    check = 1
                    break
            if check == 0:
                answer += 1

    return answer

print(solution("17"))