n = int(input())
nums = 0
for i in range(n):
  num = list(bin(int(input())))
  num = num[2:]
  result = []
  l = len(num)
  for j in range(l-1,-1,-1):
    if num[j] == "1":
      result.append(str(l - j-1))
  print(' '.join(result))