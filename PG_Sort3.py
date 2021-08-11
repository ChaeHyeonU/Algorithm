def solution(citations):
    answer = 0
    citations = sorted(citations)
    n = len(citations)
    for i, num in enumerate(citations):
        if n - i <= num:
            return n - i
    return answer