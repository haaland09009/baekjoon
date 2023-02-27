# https://www.acmicpc.net/problem/7562
# 7562 나이트의 이동
from collections import deque
import sys
input = sys.stdin.readline
# 이동할 수 있는 경우
move_types = [(-1,-2), (-2,-1), (-2,1), (-1,2), (1,-2),(2,-1),(2,1),(1,2)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        if x == target_x and y == target_y: # 목표 지점에 도착하였다면
            break
        else:
            for i,j in move_types:
                nx = x + i
                ny = y + j
                if nx < 0 or nx >= l or ny < 0 or ny >= l:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))
    return graph[target_x][target_y]      

 
t = int(input())
for _ in range(t):
    l = int(input()) # 체스판 한 변의 길이 (lxl)
    graph = [[0]*l for _ in range(l)]
    x,y = map(int,input().split()) # 현재 지점
    target_x, target_y = map(int,input().split()) # 목표 지점
    print(bfs(x,y))

