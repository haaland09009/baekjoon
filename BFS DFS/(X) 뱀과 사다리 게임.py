# https://www.acmicpc.net/problem/16928
from collections import deque

n, m = map(int,input().split())
graph = [i for i in range(101)]
distance = [0] * 101

for i in range(n+m):
    x,y = map(int,input().split())
    graph[x] = y

num = 1
q = deque([num])

while num != 100:
    num = q.popleft()
    for j in range(1, 7):
        if num + j <= 100:
            if distance[graph[num+j]] == 0:
                q.append(graph[num+j])
                distance[graph[num+j]] = distance[num] + 1

print(distance[100])