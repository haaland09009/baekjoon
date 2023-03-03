# https://www.acmicpc.net/problem/7576
from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

q = deque()

# 상하좌우 이동
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx,ny))

answer = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))

print(answer - 1)







        



