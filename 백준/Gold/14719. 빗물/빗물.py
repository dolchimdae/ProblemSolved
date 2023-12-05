h, w = map(int, input().split())
board = [[-1] * w for _ in range(h)]
full = list(map(int, input().split()))

for i in range(w):
  for j in range(full[i]):
    board[j][i] = 1

for i in range(h):
  start = False
  stack = []
  for j in range(w):
    if board[i][j] == 1 and start:
      while stack:
        a, b = stack.pop()
        board[a][b] = 2
      start = False
    if board[i][j] == -1:
      if j > 0 and board[i][j - 1] == 1:
        start = True
        stack.append([i, j])
      elif start:
        stack.append([i, j])

total = 0
for i in range(h):
  total += board[i].count(2)
print(total)
