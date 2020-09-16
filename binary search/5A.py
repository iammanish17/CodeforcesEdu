# By manish.17, contest: ITMO Academy. Двоичный поиск - 5, problem: (A) K-th Number in the Union of Segments
# https://codeforces.com/profile/manish.17

n, k = map(int, input().split())
k += 1
segments = []
for i in range(n):
    segments += [list(map(int, input().split()))]

def count(n):
    ans = 0
    for l, r in segments:
        if n >= r:
            ans += (r - l + 1)
        elif l <= n < r:
            ans += (n - l + 1)
    return ans
alpha, omega = -2*10**9, 2*10**9
while alpha < omega:
    mid = (alpha + omega) // 2
    if count(mid) >= k:
        omega = mid
    else:
        alpha = mid + 1
print(omega if count(omega-1) != k else omega - 1)
