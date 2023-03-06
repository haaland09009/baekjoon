# https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline
n = int(input())

stack = []
for _ in range(n):
    word = input().split()
    if word[0] == 'push': 
        stack.append(int(word[1])) # 정수 x를 스택에 넣기
    elif word[0] == 'top': # 스택의 가장 위에 있는 정수를 출력
        if len(stack) == 0: # 스택에 들어있는 정수가 없는 경우에는 -1을 출력
            print(-1)
        else:
            print(stack[-1])
    elif word[0] == 'size': # 스택에 들어있는 정수의 개수를 출력
        print(len(stack))                
    elif word[0] == 'empty':
        if len(stack) == 0: # 스택이 비어있으면 1
            print(1)
        else: # 아니면 0
            print(0)
    elif word[0] == 'pop': # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력
        if len(stack) == 0: #  스택에 들어있는 정수가 없는 경우에는 -1을 출력
            print(-1)
        else:
            print(stack.pop())                    