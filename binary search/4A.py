# By manish.17, contest: ITMO Academy. Двоичный поиск - 4, problem: (A) Maximum Average Segment
# https://codeforces.com/profile/manish.17

n, d = map(int, input().split())
n += 1
a = [0] + list(map(int, input().split()))

alpha, omega = 0, 100
ind = [-1,-1]
while alpha < omega:
    mid = (alpha + omega + 10**-8) / 2
    pre = [a[0] - mid]
    for i in range(1, n): pre += [pre[-1] + a[i] - mid]
    pre_min = [pre[0]]
    for i in range(1, n): pre_min += [min(pre[i], pre_min[-1])]
    pos = False
    for j in range(d, n):
        if pre_min[j - d] <= pre[j]:
            pos = True
            ind[1] = j
            ind[0] = pre.index(pre_min[j-d]) + 1
            break
    if pos:
        alpha = mid
    else:
        omega = mid - 10**-8

print(*ind)
