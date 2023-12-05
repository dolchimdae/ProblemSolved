from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))  # + - * %
ops_ = list("+" * ops[0] + "-" * ops[1] + "*" * ops[2] + "%" * ops[3])
# print(ops_)

options = set(list(permutations(ops_)))
# print(options)

max_ = -10**9
min_ = 10**9
for option in options:
  result = nums[0]
  for i in range(len(option)):
    if option[i] == '+':
      result += nums[i+1]
    elif option[i] == '-':
      result -= nums[i+1]
    elif option[i] == '*':
      result *= nums[i+1]
    else:
      if result < 0:
        result = -result // nums[i + 1]
        result *= -1
      else:
        result = result // nums[i + 1]
  if max_ < result:
    max_ = result
  if min_ > result:
    min_ = result
  
print(max_)
print(min_)
