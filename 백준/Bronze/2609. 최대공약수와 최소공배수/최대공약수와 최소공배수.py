import math

a, b = map(int, input().split())

result1 = math.gcd(a,b)
result2 = math.lcm(a,b)

print(result1)
print(result2)
