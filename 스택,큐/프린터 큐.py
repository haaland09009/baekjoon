# https://www.acmicpc.net/problem/1966
from collections import deque
t = int(input()) # 테스트 케이스의 수
for _ in range(t):
    n,m = map(int,input().split()) # 문서의 개수, 몇번 째로 인쇄되는지 궁금한 문서의 index
    arr = list(map(int,input().split())) # 문서의 중요도 리스트
    q = deque([(i,v) for i,v in enumerate(arr)]) # index, 중요도 같이 담는 리스트 생성
    
    cnt = 0
    while q:
        job = q.popleft()
        if any(job[1] < other_job[1] for other_job in q): # 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
            q.append(job)
        else:
            if m == job[0]: # 인쇄된 문서가 궁금한 문서의 index와 일치하다면
                cnt += 1
                print(cnt)
                break
            else:
                cnt += 1



