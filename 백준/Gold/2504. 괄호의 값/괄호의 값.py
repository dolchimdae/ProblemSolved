s = input()
# () 이거나 [] 이면 각각 2,3
# (x) 이거나 [x] 이면 각각 2*, 3*
stack = []
result = 0
temp = 1
l = len(s)
for i in range(l):
  b = s[i]
  if b == "(":
    temp *= 2
    stack.append(b)
  elif b == "[":
    temp *= 3
    stack.append(b)
  elif b == ")":
    if not stack or stack[-1] == "[":
      result = 0
      break
    if s[i-1] == "(":
      result += temp
    temp //= 2
    stack.pop()
  else: ## ] 인 경우
    if not stack or stack[-1] == "(":
      result = 0
      break
    if s[i-1] == "[":
      result += temp
    temp //= 3
    stack.pop()
if stack:
  result = 0

print(result)
