# By manish.17, contest: ITMO Academy. Двоичный поиск - 2, problem: (E) Equation
# https://codeforces.com/profile/manish.17

c = float(input())
alpha, omega = 1, c
while alpha < omega:
 mid = (alpha+omega)/2
 if mid**2 + mid**0.5 > c: omega = mid - 10**-7
 else: alpha = mid + 10**-7
print(alpha)
