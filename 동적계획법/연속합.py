# https://www.acmicpc.net/problem/1912

# 리스트 순회하면서
# 현재 위치에 있는 수를 현재 위치에 있는 수 + 이전 위치에 있는 수를 하였을 때 값을 비교하여
# 더 큰 값으로 변경한다.

n = int(input())
arr = list(map(int,input().split()))

for i in range(1, len(arr)):
    arr[i] = max(arr[i], arr[i-1] + arr[i])

print(max(arr))
    
