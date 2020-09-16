# By manish.17, contest: ITMO Academy. Двоичный поиск - 5, problem: (B) Multiplication Table
# https://codeforces.com/profile/manish.17

n, k = map(int, input().split())

def count(x, n):
    ans = 0
    for i in range(1, n+1):
        ans += min(n, x // i)
    return ans
alpha, omega = 1, n**2
while alpha < omega:
    mid = (alpha + omega) // 2
    if count(mid, n) >= k:
        omega = mid
    else:
        alpha = mid + 1
print(omega if count(omega-1, n) != k else omega - 1)
