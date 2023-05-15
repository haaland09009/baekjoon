# https://www.acmicpc.net/problem/1012 
# 1012 유기농 배추
from collections import deque
import sys
input = sys.stdin.readline

# 상하좌우 이동
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    global cnt
    q = deque()
    q.append((x,y))
    cnt = 1 # 배추가 심어진 수
    graph[x][y] = 0 # 방문한 좌표는 0으로 변경하여 재방문하지 않도록 한다.
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                cnt += 1
                q.append((nx,ny))
                graph[nx][ny] = 0 # 방문한 좌표는 0으로 변경하여 재방문하지 않도록 한다.
    return cnt                

t = int(input()) # 테스트 케이스의 개수
for _ in range(t):
    m,n,k = map(int,input().split()) # 가로, 세로, 배추 개수
    graph = [[0]*n for _ in range(m)]
    for _ in range(k):
        x,y = map(int,input().split()) # 배추가 심어진 좌표는 1로 변경
        graph[x][y] = 1
    answer = [] # 배추가 심어진 좌표를 만났을 때 bfs 실행 -> 상하좌우 주변에 배추가 심어진 수 체크 ->
    # 사실 각 배추가 심어진 수는 중요하지 않다.
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1: # 그래프 순회 중에 배추가 심어진 곳에 도달한다면 bfs 실행
                answer.append(bfs(i,j))   
    print(len(answer))                 
    
    
    
    
# from collections import deque
# import sys
# input = sys.stdin.readline

# dx = [0,0,-1,1]
# dy = [-1,1,0,0]

# def bfs(x,y):
#     global cnt
#     q = deque()
#     q.append((x,y))
#     graph[x][y] = 0
#     cnt = 1
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= m or ny < 0 or ny >= n:
#                 continue
#             if graph[nx][ny] == 1:
#                 cnt += 1
#                 graph[nx][ny] = 0
#                 q.append((nx,ny))
#     return cnt            


# t = int(input())
# for _ in range(t):
#     answer = []
#     m,n,k = map(int,input().split())
#     graph = [[0]*n for _ in range(m)]
#     for _ in range(k):
#         x,y = map(int,input().split())
#         graph[x][y] = 1
#     for i in range(m):
#         for j in range(n):
#             if graph[i][j] == 1:
#                 answer.append(bfs(i,j))
#     print(len(answer))        
   
    



