def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n-1):
        cnt = 0
        for j in range(i+1,n):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    answer.append(0)
    return answer