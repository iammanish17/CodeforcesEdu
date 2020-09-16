# By manish.17, contest: ITMO Academy. Двоичный поиск - 2, problem: (G) Student Councils
# https://codeforces.com/profile/manish.17

k = int(input())
n = int(input())
a = []
for i in range(n):
    a += [int(input())]

alpha, omega = 1, 10**18
while alpha < omega:
    mid = (alpha + omega + 1) // 2
    total = k*mid
    for i in range(n):
        total -= min(mid, a[i], total)
    if total == 0:
        alpha = mid
    else:
        omega = mid - 1
print(omega)
