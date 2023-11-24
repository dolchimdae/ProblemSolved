from itertools import product
import re

able = set()
def solution(user_id, banned_id):
    '''
    가리고자 하는 문자 하나에 * 사용. 아이디 당 최소 하나 이상 사용
    불량 사용자 목록에 매핑된 아이디 => 제재 아이디라고 부르기로.
    '''
    hubo = []
    temp = list(set(banned_id))
    ##
    johap = []
    for bid in banned_id:
        hubo = []
        new = ""
        for b in bid:
            if b == "*":
                new += "\w"
            else:
                new += b
        print(new)
        pattern = re.compile(new)
        hubo = [id for id in user_id if pattern.match(id) and len(id) == len(bid)]
        johap.append(hubo)
        
    # for bid in banned_id:
    #     hubo = []
    #     l = len(bid)
    #     idx = []
    #     bl = len(bid)
    #     for i in range(bl):
    #         if bid[i] != "*":
    #             idx.append(i)
    #     for uid in user_id:
    #         # 길이 같고 idx 있는 부분 일치
    #         if  len(uid) == l:
    #             same = True
    #             for x in idx:
    #                 if uid[x] != bid[x]:
    #                     same = False
    #                     break
    #             if same:
    #                 hubo.append(uid)
    #     print(hubo)
    #     johap.append(hubo)
    # print(johap)
    generate_combinations(johap)
    answer = len(able)
    return answer

def generate_combinations(lists, current=[]):
    if not lists:
        if len(set(current)) != len(current):
            return
        able.add(''.join(sorted(current)))
        return
    for item in lists[0]:
        if item not in lists:
            generate_combinations(lists[1:], current + [item])

