# https://www.acmicpc.net/problem/11866
from collections import deque
n,k = map(int,input().split())

q = deque([i for i in range(1, n+1)])

answer = '<'
while q:
    for i in range(k-1):
        now = q.popleft()
        q.append(now)
    x = q.popleft()
    if len(q) == 0:
        answer += str(x)
    else:       
        answer += (str(x) + ', ')
answer += '>'

print(answer)


        
        
