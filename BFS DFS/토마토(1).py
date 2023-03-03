# https://www.acmicpc.net/problem/7569

from collections import deque
import sys
input = sys.stdin.readline
m,n,h = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

q = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                q.append((k,i,j))

dz = [0,0,0,0,-1,1]
dx = [0,0,-1,1,0,0]
dy = [-1,1,0,0,0,0]

while q:
    z,x,y = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nz][nx][ny] == 0:
            graph[nz][nx][ny] = graph[z][x][y] + 1
            q.append((nz,nx,ny))

answer = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                print(-1)
                exit(0)
            else:
                answer = max(answer, graph[k][i][j])

print(answer-1)                    
