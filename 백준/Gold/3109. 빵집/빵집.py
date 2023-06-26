r,c = map(int, input().split())
## r행 c열
board = []
visited = [[-1]*c for _ in range(r)]
answer = 0
for _ in range(r):
  board.append(list(input()))

def dfs(cr,cc):
  if cc == c-1:
    return True
  for dr in [-1,0,1]: ##
    nr = cr + dr
    nc = cc + 1
    if 0 <= nr < r and 0 <= nc < c:
      if board[nr][nc] != 'x' and visited[nr][nc] == -1:
        visited[nr][nc] = 1
        if dfs(nr,nc):
          return True
  return False

for i in range(r):
  if dfs(i,0):
    answer += 1

print(answer)


