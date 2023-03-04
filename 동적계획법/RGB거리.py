# https://www.acmicpc.net/problem/1149
n = int(input()) # 집의 수
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in range(1, n):
    for j in range(len(arr[i])):
        arr[i][j] =  arr[i][j] + min(arr[i-1][:j] + arr[i-1][j+1:])
        # ex) 리스트끼리의 덧셈: [1] + [2,3] = [1,2,3]

print(min(arr[-1])) # 리스트의 마지막 행에 있는 값에서 가장 작은 값이 정답