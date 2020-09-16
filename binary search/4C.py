# By manish.17, contest: ITMO Academy. Двоичный поиск - 4, problem: (C) Pair Selection
# https://codeforces.com/profile/manish.17

n, k = map(int, input().split())
pairs = []
for i in range(n):
    a, b = map(int, input().split())
    pairs += [[a, b]]

alpha, omega = 0, 10**18
while alpha < omega:
    mid = (alpha + omega)/2
    if mid == alpha:break
    queue = []
    for a, b in pairs:
        # sum(a[i]) / sum(b[i]) >= mid
        # sum(a[i] - mid*b[i]) >= 0
        queue += [a - b*mid]
    ans = sum(sorted(queue,reverse=True)[:k])
    if ans >= 0:
        alpha = mid
    else:
        omega = mid - 10**-8

print(omega)
