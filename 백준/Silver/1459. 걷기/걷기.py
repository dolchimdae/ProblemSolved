## x y 위치 w 가로세로 s 대각선 걸리는 시간
x,y,w,s = map(int, input().split())
answer = 0

if(2*w < s):
  answer = (x+y)*w
else:
  if(x>y):
    left = x-y
    answer = y*s
  else:
    left = y-x
    answer = x*s
  if s < w:
    answer += (left//2)*2*s+(left%2)*w
  else:
    answer += left*w
    
print(answer)