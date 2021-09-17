
def solution(s):
    answer = ""
    while s:
        try:
            answer += str(int(s[0]))
            s = s[1:]
        except:
            input = ""
            if s.startswith("z"):
                input = '0'
                s = s[4:]
                #s = s.replace('zero', '')
            elif s.startswith('o'):
                input = '1'
                s = s[3:]
                #s = s.replace('one', '')
            elif s.startswith('tw'):
                input = '2'
                s = s[3:]
                #s = s.replace('two', '')
            elif s.startswith('th'):
                input = '3'
                s = s[5:]
                #s = s.replace('three', '')
            elif s.startswith('fo'):
                input = '4'
                s = s[4:]
                #s = s.replace('four', '')
            elif s.startswith('fi'):
                input = '5'
                s = s[4:]
                #s = s.replace('five', '')
            elif s.startswith('si'):
                input = '6'
                s = s[3:]
                #s = s.replace('six', '')
            elif s.startswith('se'):
                input = '7'
                s = s[5:]
                #s = s.replace('seven', '')
            elif s.startswith('e'):
                input = '8'
                s = s[5:]
                #s = s.replace('eight', '')
            elif s.startswith('n'):
                input = '9'
                s = s[4:]
                #s = s.replace('nine', '')
            answer += input

    return int(answer)

print(solution("one4seveneight"))