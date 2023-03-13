# https://www.acmicpc.net/problem/3273
import sys
input = sys.stdin.readline
n = int(input()) # 수열의 크기
arr = list(map(int,input().split()))
x = int(input())

arr.sort() # 배열을 오름차순 정렬
answer = 0
left, right = 0, len(arr)-1

while left < right:
    if arr[left] + arr[right] > x:
        right -= 1
    elif arr[left] + arr[right] < x:
        left += 1
    elif arr[left] + arr[right] == x:
        answer += 1
        right -= 1

print(answer)
