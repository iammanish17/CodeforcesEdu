# By manish.17, contest: ITMO Academy. Двоичный поиск - 4, problem: (B) Minimum Average Path
# https://codeforces.com/profile/manish.17

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
weights = []
for i in range(m):
    a, b, w = map(int, input().split())
    weights += [[a,b,w]]

weights = sorted(weights, key=lambda x: x[0])

alpha, omega = 0, 1000
while alpha < omega:
    mid = (alpha + omega) / 2
    if mid == omega:break
    dp = [10**18]*(n+1)
    dp[1] = 0
    for a, b, w in weights:
        dp[b] = min(dp[b], dp[a] + w - mid)
    if dp[n] <= 0:
        omega = mid
    else:
        alpha = mid + 10**-8

came_from = [0]*(n+1)
dp = [10**18]*(n+1)
dp[1] = 0
for a, b, w in weights:
    if dp[a] + w - mid <= dp[b]:
        dp[b] = dp[a] + w - mid
        came_from[b] = a

path = [n]
x = n
while came_from[x] != 1:
    x = came_from[x]
    path += [x]
path += [1]
print(len(path) - 1)
print(*path[::-1])
