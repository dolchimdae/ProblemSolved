def solution(s):
    nums = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    temp = s
    i = 0
    answer = ""
    while temp:
        if temp[:3] in nums:
            answer += str(nums.index(temp[:3]))
            temp = temp[3:]
        elif temp[:4] in nums:
            answer += str(nums.index(temp[:4]))
            temp = temp[4:]
        elif temp[:5] in nums:
            answer += str(nums.index(temp[:5]))
            temp = temp[5:]
        else:
            answer += temp[0]
            temp = temp[1:]
    answer = int(answer)
    return answer