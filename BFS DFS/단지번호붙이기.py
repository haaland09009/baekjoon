# https://www.acmicpc.net/problem/2667

from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

# 상하좌우 이동좌표 명시
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    global cnt 
    q = deque()
    q.append((x,y)) 
    cnt = 1 # 각 단지 내 집의 수를 담을 변수
    graph[x][y] = 0 # 이미 방문한 것은 재방문하지 않기 위해 0으로 표시
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                cnt += 1
                q.append((nx,ny))
                graph[nx][ny] = 0 # 이미 방문한 것은 재방문하지 않기 위해 0으로 표시
    return cnt            

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 그래프 순회 시 1을 만나게 되면 bfs 실행
            answer.append(bfs(i,j))              

answer.sort()
print(len(answer))
for i in answer:
    print(i)
