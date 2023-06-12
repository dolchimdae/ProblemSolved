def solution(number, k):
    # 선택한 숫자들을 저장할 스택
    stack = []  
    for num in number:
        # 현재 숫자보다 작은 숫자가 스택에 있으면 제거
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    # k개의 숫자를 제거하지 못한 경우 남은 숫자들 중에서 뒤에서부터 k개 제거
    while k > 0:
        stack.pop()
        k -= 1
    answer = ''.join(stack)
    return answer

##  시간 초과   ##
# def solution(number, k):
#     answer = ''
#     answerLen = 0
#     tempNum = number
#     while answerLen < k :
#         tempMax = tempNum[1:]
#         # print(tempMax)
#         n = len(tempNum)
#         for i in range(n):
#             temp = tempNum[:i]+tempNum[i+1:]
#             # print("?",temp)
#             if(temp > tempMax):
#                 tempMax = temp
#                 # print("tempMax",tempMax)
#         tempNum = tempMax
#         answerLen += 1
#         # print(answerLen)
#     answer = tempNum
#     return answer

