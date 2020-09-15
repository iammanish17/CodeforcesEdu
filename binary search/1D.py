# By manish.17, contest: ITMO Academy. Двоичный поиск - 1, problem: (D) Fast search
# https://codeforces.com/profile/manish.17

from bisect import bisect_left, bisect_right

class Result:
    def __init__(self, index, value):
        self.index = index
        self.value = value

class BinarySearch:
    def __init__(self):
        pass

    @staticmethod
    def greater_than(num: int, func, size: int = 1):
        """Searches for smallest element greater than num!"""
        if isinstance(func, list):
            index = bisect_right(func, num)
            if index == len(func):
                return Result(None, None)
            else:
                return Result(index, func[index])
        else:
            alpha, omega = 0, size - 1
            if func(omega) <= num:
                return Result(None, None)
            while alpha < omega:
                if func(alpha) > num:
                    return Result(alpha, func(alpha))
                if omega == alpha + 1:
                    return Result(omega, func(omega))
                mid = (alpha + omega) // 2
                if func(mid) > num:
                    omega = mid
                else:
                    alpha = mid

    @staticmethod
    def less_than(num: int, func, size: int = 1):
        """Searches for largest element less than num!"""
        if isinstance(func, list):
            index = bisect_left(func, num) - 1
            if index == -1:
                return Result(None, None)
            else:
                return Result(index, func[index])
        else:
            alpha, omega = 0, size - 1
            if func(alpha) >= num:
                return Result(None, None)
            while alpha < omega:
                if func(omega) < num:
                    return Result(omega, func(omega))
                if omega == alpha + 1:
                    return Result(alpha, func(alpha))
                mid = (alpha + omega) // 2
                if func(mid) < num:
                    alpha = mid
                else:
                    omega = mid


import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))

bs = BinarySearch()
b = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    ind1 = bs.greater_than(x-1, a).index
    ind2 = bs.less_than(y+1, a).index
    if ind1 is None: ind1 = n+1
    if ind2 is None: ind2 = -1
    b += [max(0, ind2-ind1+1)]
print(*b)
