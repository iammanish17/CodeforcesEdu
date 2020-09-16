# By manish.17, contest: ITMO Academy. Двоичный поиск - 3, problem: (C) Cows in Stalls
# https://codeforces.com/profile/manish.17

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))

alpha, omega = 0, a[-1] - a[0]
while alpha < omega:
    mid = (alpha + omega + 1) // 2
    ans = 1
    cur = a[0]
    for i in range(1, n):
        if a[i] >= cur + mid:
            cur = a[i]
            ans += 1
    if ans >= k:
        alpha = mid
    else:
        omega = mid - 1
print(omega)
