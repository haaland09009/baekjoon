# https://www.acmicpc.net/problem/2579
n = int(input())
s = [0] * 100001

for i in range(1, n+1):
    s[i] = int(input())

a = [0] * 10001

a[1] = s[1]
a[2] = s[1] + s[2]
a[3] = max(s[1]+s[3], s[2]+s[3])

for i in range(4, n+1):
    a[i] = max(a[i-2]+s[i], a[i-3]+s[i-1]+s[i])

print(a[n])