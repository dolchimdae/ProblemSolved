from collections import deque

n = int(input())
for i in range(n):
  dn,M = map(int, input().split()) 
  # 문서의 개수,몇번째로 인쇄됐는지나타내는 정수
  l = list(map(int,input().split()))
  q = deque([(l[i], i) for i in range(len(l))])
  result = 0
  while q:
    cur, curIdx = q.popleft()
    if q and cur < max(q)[0]:
      q.append((cur,curIdx))
      continue
    else:
      result += 1
      if curIdx == M:
        print(result)
        break
    
        
      
        
    
    
  