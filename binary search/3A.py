# By manish.17, contest: ITMO Academy. Двоичный поиск - 3, problem: (A) Get together
# https://codeforces.com/profile/manish.17

n = int(input())
pairs = []
for i in range(n):
    pairs += [list(map(int, input().split()))]

alpha, omega = 0, 10**9
while alpha < omega:
    mid = (alpha+omega)/2
    if mid == omega:break
    pos = True
    segment = [-10**18, 10**18]
    for x, v in pairs:
        left, right = x - mid*v, x + mid*v
        if min(segment[1], right) >= max(segment[0], left):
            segment[0], segment[1] = max(segment[0], left), min(segment[1], right)
        else:
            pos = False
            break
    if pos:
        omega = mid
    else:
        alpha = mid + 10**-8
print(omega)
