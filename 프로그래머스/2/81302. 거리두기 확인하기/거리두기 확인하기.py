def dfs(x,y, place):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    ddx = [1,1,-1,-1]
    ddy = [1,-1,1,-1]
    dddx = [2,-2,0,0]
    dddy = [0,0,-2,2]
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx > 4 or nx < 0 or ny > 4 or ny < 0:
            continue
        if place[nx][ny] == "P":
            return False
    for i in range(4):
        nx = ddx[i] + x
        ny = ddy[i] + y
        if nx > 4 or nx < 0 or ny > 4 or ny < 0:
            continue
        if place[nx][ny] == "P": ## 대각선
            if place[nx][y] != "X" or place[x][ny]  != "X":
                return False
    for i in range(4):
        nx = dddx[i] + x
        ny = dddy[i] + y
        mx = dx[i] + x
        my = dy[i] + y
        if nx > 4 or nx < 0 or ny > 4 or ny < 0:
            continue
        if place[nx][ny] == "P": ## 2
            if place[mx][my] != "X" or place[mx][my]  != "X":
                return False
    return True

def placeChecker(place):
    for x in range(5):
        for y in range(5):
            if place[x][y] == "P" and dfs(x,y,place)== False:
                return False
    return True

def solution(places):
    '''
    맨해튼 거리 : |r1 - r2| + |c1 - c2|
    5*5 , 맨해튼 거리가 2이하로 앉지 말기... 파티션으로 막혀있으면 허용.
    빈테이블 : 0, 파티션: X, 응시자가 앉아있는 자리 P
    '''
    answer = []
    for place in places:
        if placeChecker(place) == True:
            answer.append(1)
            
        else:
            answer.append(0)
            

    return answer