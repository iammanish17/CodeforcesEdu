# By manish.17, contest: ITMO Academy. Двоичный поиск - 2, problem: (A) Packing Rectangles
# https://codeforces.com/profile/manish.17

w, h, n = map(int, input().split())

alpha, omega = 1, 10**18

while alpha < omega:
    mid = (alpha+omega)//2
    if mid < max(w, h):
        alpha = mid + 1
        continue
    count = (mid // w)*(mid // h)
    if count >= n:
        omega = mid
    else:
        alpha = mid + 1

print(omega)
