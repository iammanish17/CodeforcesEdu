# By manish.17, contest: ITMO Academy. Двоичный поиск - 5, problem: (C) K-th Sum
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


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(list(map(int, input().split())))
bs = BinarySearch()
def count(x):
    ans = 0
    for i in a:
        index = bs.less_than(x - i + 1, b).index
        if index is not None: ans += (index + 1)
    return ans

alpha, omega = 1, 10**18
while alpha < omega:
    mid = (alpha + omega) // 2
    if count(mid) >= k:
        omega = mid
    else:
        alpha = mid + 1
print(omega if count(omega-1) != k else omega - 1)
