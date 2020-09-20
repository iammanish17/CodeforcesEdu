# By manish.17, contest: ITMO Academy. Дерево отрезков 2 - 1, problem: (B) Applying MAX to Segment
# https://codeforces.com/profile/manish.17

from math import log2


class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.size = 2**(int(log2(self.n-1))+1) if self.n != 1 else 1
        self.default = 0
        self.data = [self.default] * (2 * self.size)
        self.process(array)

    def process(self, array):
        self.data[self.size : self.size+self.n] = array

    def query(self, index):
        """Returns the value at given index!"""
        res = self.default
        index += self.size
        while index:
            res = max(res, self.data[index])
            index >>= 1
        return res

    def update(self, alpha, omega, value):
        alpha += self.size
        omega += self.size + 1
        while alpha < omega:
            if alpha & 1:
                self.data[alpha] = max(self.data[alpha], value)
                alpha += 1
            if omega & 1:
                omega -= 1
                self.data[omega] = max(self.data[omega], value)
            alpha >>= 1
            omega >>= 1

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
st = SegmentTree([0]*n)
for _ in range(m):
    a = list(map(int, input().split()))
    if a[0] == 1:
        st.update(a[1], a[2]-1, a[3])
    else:
        print(st.query(a[1]))
