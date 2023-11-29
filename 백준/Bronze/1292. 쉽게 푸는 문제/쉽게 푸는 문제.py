
a,b = map(int,input().split())

nums = []
cur = 1
while len(nums) <= b:
  nums += [cur]*cur
  cur += 1
print(sum(nums[a-1:b]))


