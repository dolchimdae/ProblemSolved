def solution(genres, plays):
    answer = []
    n = len(genres)
    dic = dict()
    for i in range(n):
        if genres[i] in dic.keys():
            dic[genres[i]] += plays[i]
        else:
            dic[genres[i]] = plays[i]
            
    gen_total = list([d,dic[d]] for d in dic)
    gen_total.sort(key = lambda x : (x[1]),reverse=True)
    # print(gen_total)
    
    rank = dict()
    i = 0
    for g in gen_total:
        rank[g[0]] = i
        i+=1
        
    final = []
    for i in range(n):
        final.append([rank[genres[i]],plays[i],i])
        
    final.sort(key = lambda x : (x[0],-x[1], x[2]))
    # print(final)
    cur = [final[0],2]
    for f in final:
        if cur[0] == f[0]:
            if cur[1] == 0:
                continue
            else:
                cur[1] -= 1
                answer.append(f[2])
        else :
            cur=[f[0],1]
            answer.append(f[2])
            
    return answer