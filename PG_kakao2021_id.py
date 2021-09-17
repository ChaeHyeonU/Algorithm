def solution(new_id):

    answer = new_id.lower()
    spchar = "~!@#$%^&*()=+[{]}:?,<>/"
    for i in spchar:
        answer = answer.replace(i,"")

    while True:
        if answer.find("..") != -1:
            answer = answer.replace("..",".")
        else:
            break
    answer = answer.strip(".")
    if len(answer) < 1:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.strip(".")
    while len(answer) < 3:
        answer += answer[-1]
    return answer

print(solution(	"............!@BaT#*..y.abcdefghijklm"))