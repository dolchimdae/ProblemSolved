def solution(s):
    '''
    n-튜플 : n개 요소
    중복가능. 원소 각각 순서있고 순서 다르면 구별됨
    원소 개수는 유한함
    중복되는 원소가 없는 튜플이 주어질 때 이는 { }.
    '''
    s =  s[2:-2]
    temp = []
    if "},{" in s:
        s = s.split("},{")
        for i in range(len(s)):
            if "," in s[i]:
                temp.append((s[i].split(",")))
            else :
                temp.append([s[i]])
    else:
        temp.append(s)
    temp.sort(key = lambda x: len(x))
    answer = []
    idx = 0
    if len(temp) == 1:
        return [int(temp[0])]
    while idx < len(temp):
        for t in temp[idx]:
            if t in answer:
                continue;
            else:
                answer.append(t)
        idx += 1
    answer = list(map(int,answer))
    return answer