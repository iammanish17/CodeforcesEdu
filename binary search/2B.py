# By manish.17, contest: ITMO Academy. Двоичный поиск - 2, problem: (B) Ropes
# https://codeforces.com/profile/manish.17

n, k = map(int, input().split())
a = []
for i in range(n):
    a += [float(input())]

alpha, omega = 10**-8, 10**18

while alpha < omega:
    mid = (alpha+omega)/2
    if mid == alpha:break
    parts = sum([int(k // mid) for k in a])
    if parts >= k:
        alpha = mid
    else:
        omega = mid - 10**-8


print(omega)
