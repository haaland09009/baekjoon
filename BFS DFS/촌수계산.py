from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    q = deque([s])
    visited[s] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                result[i] = result[now] + 1
                q.append(i)

n = int(input())
a,b = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = [0] * (n+1)

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a)

if result[b] > 0:
    print(result[b])
else:  # 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때
    print(-1)    