
def solution(n, times):
    min_time = 1
    max_time = max(times) * n
    ans = 1

    while min_time <= max_time:
        mid = (min_time + max_time) // 2
        print(min_time, mid, max_time)
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        print(people, ans)
        if people >= n:
            ans = mid
            max_time = mid - 1
        else:
            min_time = mid + 1
    return ans

print(solution(6, [7, 10]))