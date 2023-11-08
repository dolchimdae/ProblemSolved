from collections import deque

def solution(queue1, queue2):
    '''
    하나의 큐에 pop 다른 큐에 insert 해서 각 큐 원소합 ==
    위작업이 1회. 큐라서 선입선출.
    '''
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    goal = (sum(q1)+sum(q2))/2
    if goal % 1 != 0:
        return -1
    answer = 0
    l = len(q1)
    s1 = sum(q1)
    s2 = sum(q2)
    while s1 != s2 and s1 != goal:
        from1 = abs(s1-q1[0]-goal)+abs(s2+q1[0]-goal)
        from2 = abs(s2-q2[0]-goal)+abs(s1+q2[0]-goal)
        if from1 < from2:
            temp = q1.popleft()
            q2.append(temp)
            s2 += temp; s1 -= temp
        else:
            temp = q2.popleft()
            q1.append(temp)
            s1 += temp; s2 -= temp
        answer += 1
        if answer > l*3:
            answer = -1
            break
    return answer