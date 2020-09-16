# By manish.17, contest: ITMO Academy. Двоичный поиск - 2, problem: (D) Children Holiday
# https://codeforces.com/profile/manish.17

m, n = map(int, input().split())
if m == 0:
    print(0)
    print(*[0]*n)
    quit()
a = []
for i in range(n):
    t, z, y = map(int, input().split())
    a += [[t, z, y]]

alpha, omega = 1, 10**18
while alpha < omega:
    mid = (alpha + omega) // 2
    ans = 0
    for t,z,y in a:ans += z*(mid//(t*z + y)) + min(z,(mid % (t*z + y))//t)
    if ans >= m:
        omega = mid
    else:
        alpha = mid + 1
print(omega)
b = [z*(omega//(t*z + y)) + min(z,(omega % (t*z + y))//t) for t, z, y in a]
total = 0
for i in range(n):
    b[i] = min(b[i], m - total)
    total += b[i]
print(*b)
