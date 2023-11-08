def solution(survey, choices): ## 지표, 선택지
    ''' AB 일떄 A는 비동의 B는 동의
    1 매우 비동의 2 비동 3약비 4 00 5약동 6동 7매동
    R   T
    C   f   
    J   M
    A   N
    같으면 사전순.
    '''
    l = len(survey)
    dic = dict()
    for i in range(l): ## 4보다 작으면 4에서 빼고 이상이면 4를 빼야.
        s = survey[i]
        b = s[0]; d = s[1];
        if choices[i] < 4 :
            if b not in dic:
                dic[b] = (4-choices[i])
            else:
                dic[b] += (4-choices[i])
        else:
            if d not in dic:
                dic[d] = (choices[i]-4)
            else:
                dic[d] += (choices[i]-4)
    result = []
    for a,b in [["R","T"],["C","F"],["M","J"],["N","A"]]:
        if a not in dic:
            dic[a] = 0
        if b not in dic:
            dic[b] = 0
        if dic[a] > dic[b]:
            result.append(a)
        elif dic[a] == dic[b]:
            if ord(a) < ord(b):
                result.append(a)
            else:
                result.append(b)
        else:
            result.append(b)
            
    answer = ''.join(result)
    return answer