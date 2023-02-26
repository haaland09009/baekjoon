from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
t = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(t):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
cnt = 0

def bfs(v):
    global cnt
    q = deque()
    q.append(v)
    visited[v] = True # 문제에서 주어진 첫번째 노드 방문 표시
    while q:
        now = q.popleft() # 현재 queue에 있는 가장 앞에 있는 노드 꺼내기
        for i in graph[now]: # 꺼낸 노드와 인접한 노드 중에서
            if not visited[i]: # 아직 방문하지 않은 노드가 있다면
                visited[i] = True # 방문을 표시하고
                cnt += 1 # 방문한 수 추가
                q.append(i)
    return cnt

print(bfs(1))
