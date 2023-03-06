# https://www.acmicpc.net/problem/9012
import sys
input = sys.stdin.readline

def VPS(x):
    stack = []
    result = "YES" # 반복문을 돌고 나서 이상이 없으면 YES로 출력할 수 있도록 설정
    for i in x:
        if i == '(':
            stack.append(i)    
        else:
            if len(stack) == 0:
                result = "NO" # 올바르지 않은 괄호이면 NO를 출력하도록 설정하고 반복문 종료
                break
            else:
                stack.pop()    
    if stack: # 반복문을 돌고나서 스택에 원소가 있는 경우 NO 출력 
        result = "NO"
    return result   


t = int(input())
for _ in range(t):
    word = input().strip()
    print(VPS(word))




             
