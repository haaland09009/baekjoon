# https://www.acmicpc.net/problem/1021
from collections import deque
n,m = map(int,input().split())
arr = list(map(int,input().split()))

q = deque([i for i in range(1, n+1)])

cnt = 0
while arr: # arr에 있는 모든 원소를 뽑기 전까지 반복문 실행
    if q[0] == arr[0]: # 뽑으려는 원소가 queue에 있는 첫번째 원소와 같을 때
        q.popleft()
        arr.pop(0)
        if len(arr) == 0:
            break
    else:
        if q.index(arr[0]) <= len(q) // 2:
            q.rotate(-1)
            cnt += 1
        else:
            q.rotate(1)
            cnt += 1

print(cnt)


