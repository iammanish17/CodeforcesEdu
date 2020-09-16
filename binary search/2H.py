# By manish.17, contest: ITMO Academy. Двоичный поиск - 2, problem: (H) Hamburgers
# https://codeforces.com/profile/manish.17

s = input()
nb, ns, nc = map(int, input().split())
pb, ps, pc = map(int, input().split())
r = int(input())

alpha, omega = 0, 10**36
b, s, c = s.count("B"), s.count("S"), s.count("C")
while alpha < omega:
    mid = (alpha + omega + 1) // 2
    bread, sausage, cheese = max(0, b*mid - nb), max(0, s*mid - ns), max(0, c*mid - nc)
    cost = bread*pb + sausage*ps + cheese*pc
    if cost <= r:
        alpha = mid
    else:
        omega = mid - 1

print(omega)
