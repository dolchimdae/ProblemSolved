def solution(board, moves):
    answer = 0
    bag = []
    l = len(board)
    for move in moves:
        deep = 0
        none = False
        # 빈칸이면 내려가기
        while board[deep][move-1] == 0:
            deep += 1
            if deep == l:
                none = True
                break
        if none:
            continue
        else:
            bag.append(board[deep][move-1])
            board[deep][move-1] = 0
            # print("bag",bag)
        if len(bag) > 1 and bag[-2] == bag[-1]:
            bag = bag[:-2]
            answer += 2
        
    return answer