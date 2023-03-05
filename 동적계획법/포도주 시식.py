# https://www.acmicpc.net/problem/2156
n = int(input())
a = [0] * 10000
for i in range(n):
    a[i] = int(input())

dp = [0] * 10000

# 경우의 수
dp[0] = a[0]
dp[1] = a[0] + a[1]
dp[2] = max(dp[0] + a[2], a[1] + a[2], dp[1])
for i in range(3, n):
    dp[i] = max(dp[i-2] + a[i], dp[i-3] + a[i-1] + a[i], dp[i-1])

print(max(dp))



