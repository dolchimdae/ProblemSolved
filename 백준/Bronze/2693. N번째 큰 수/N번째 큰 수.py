import math

t = int(input())

for _ in range(t):
  data = list(map(int,input().split()))
  data.sort()
  print(data[-3])
