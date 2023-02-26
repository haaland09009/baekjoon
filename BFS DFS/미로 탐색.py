# https://www.acmicpc.net/problem/2178

from collections import deque
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]    

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1: # 이동할 수 있는 칸(1)이라면
                graph[nx][ny] = graph[x][y] + 1 # queue에서 꺼낸 (x,y) 값에 1을 더함
                q.append((nx,ny))    
    return graph[n-1][m-1] # 목표 좌표 return

print(bfs(0,0))

