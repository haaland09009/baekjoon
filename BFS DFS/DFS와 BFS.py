# https://www.acmicpc.net/problem/1260

from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하기 위해 오름차순으로 정렬
for i in range(n+1):
    graph[i].sort()    

visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    print(v, end=' ')
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                print(i, end=' ')
                q.append(i)

dfs(r)
visited = [False] * (n+1)
print()
bfs(r)
