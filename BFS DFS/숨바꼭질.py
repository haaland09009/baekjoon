# https://www.acmicpc.net/problem/1697
# 1697 숨바꼭질
from collections import deque
n,k = map(int,input().split())
dp = [0 for _ in range(100001)] # ! 주어진 범위를 이용하여 리스트를 생성할 것.
#                                   문제에서 주어진 범위: 점 N(0 ≤ N ≤ 100,000), 점 K(0 ≤ K ≤ 100,000)

q = deque()
q.append(n) # 현재 위치 queue에 담기
while q:
    x = q.popleft() # 현재 위치 queue에서 꺼내기
    if x == k: # 만약 꺼낸 위치가 동생이 있는 위치라면 바로 출력
        print(dp[k])
        break
    for i in (x-1, x+1, 2*x):
        if 0 <= i <= 100000 and dp[i] == 0: # 아직 방문하지 않았다면
            dp[i] = dp[x] + 1
            q.append(i)

        





