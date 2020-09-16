# By manish.17, contest: ITMO Academy. Двоичный поиск - 2, problem: (F) String Game
# https://codeforces.com/profile/manish.17

s = input()
s2 = input()
a = list(map(int, input().split()))

alpha, omega = 0, len(s) - len(s2)

while alpha < omega:
    mid = (alpha + omega + 1) // 2
    b = list(s)
    for i in range(mid):
        b[a[i]-1] = ""
    count = 0
    for i in b:
        if i == s2[count]:
            count += 1
            if count == len(s2):break
    if count == len(s2):
        alpha = mid
    else:
        omega = mid-1

print(omega)
