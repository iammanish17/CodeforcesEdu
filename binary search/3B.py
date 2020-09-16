# By manish.17, contest: ITMO Academy. Двоичный поиск - 3, problem: (B) Splitting an Array
# https://codeforces.com/profile/manish.17

n, k = map(int, input().split())
a = list(map(int, input().split()))

alpha, omega = max(a), 10**14
while alpha < omega:
    mid = (alpha + omega) // 2
    count = 1
    total = 0
    i = 0
    while i < n:
        if total + a[i] > mid:
            count += 1
            total = a[i]
        else:
            total += a[i]
        i += 1
    if count <= k:
        omega = mid
    else:
        alpha = mid + 1
print(omega)
