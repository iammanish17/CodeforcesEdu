# By manish.17, contest: ITMO Academy. Двоичный поиск - 2, problem: (C) Very Easy Task
# https://codeforces.com/profile/manish.17

n, x, y = map(int, input().split())

alpha, omega = min(x, y), 10**18
if n == 1:
    print(min(x, y))
    quit()

while alpha < omega:
    mid = (alpha + omega)//2
    if (mid - min(x, y))//x + (mid - min(x, y))//y >= n-1:
        omega = mid
    else:
        alpha = mid + 1
print(omega)
