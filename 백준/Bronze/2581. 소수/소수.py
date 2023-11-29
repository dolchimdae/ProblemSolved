
m = int(input())
n = int(input())

def sosu(n):
  if n==1:
    return False
  for i in range(n-1,1,-1):
    if n%i==0:
      return False
  return True
  
result = []

for i in range(m,n+1):
  if sosu(i):
    result.append(i)
if len(result)==0:
  print(-1)
else:
  print(sum(result))
  print(min(result))




