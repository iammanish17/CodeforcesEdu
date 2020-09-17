# By manish.17, contest: ITMO Academy. Дерево отрезков часть 1. 1, problem: (C) Number of Minimums on a Segment
# https://codeforces.com/profile/manish.17

from math import inf, log2


class SegmentTree:
    def __init__(self, array, func=max):
        self.n = len(array)
        self.size = 2**(int(log2(self.n-1))+1) if self.n != 1 else 1
        self.func = func
        self.default = 0 if self.func != min else inf
        self.data = [self.default] * (2 * self.size)
        self.count = [1] * (2 * self.size)
        self.process(array)

    def process(self, array):
        self.data[self.size : self.size+self.n] = array
        for i in range(self.size-1, -1, -1):
            self.data[i] = self.func(self.data[2*i], self.data[2*i+1])
            self.count[i] = 0
            if self.data[i] == self.data[2*i]:
                self.count[i] += self.count[2*i]
            if self.data[i] == self.data[2*i + 1]:
                self.count[i] += self.count[2*i+1]

    def query(self, alpha, omega):
        """Returns the result of function over the range (inclusive)!"""
        if alpha == omega:
            return self.data[alpha + self.size], 1
        res = self.default
        alpha += self.size
        omega += self.size + 1
        count = {}
        while alpha < omega:
            if alpha & 1:
                res = self.func(res, self.data[alpha])
                count[self.data[alpha]] = self.count[alpha] if self.data[alpha] not in count else count[self.data[alpha]] + self.count[alpha]
                alpha += 1
            if omega & 1:
                omega -= 1
                res = self.func(res, self.data[omega])
                count[self.data[omega]] = self.count[omega] if self.data[omega] not in count else count[self.data[omega]] + \
                                                                                               self.count[omega]
            alpha >>= 1
            omega >>= 1
        return res, count[res]

    def update(self, index, value):
        """Updates the element at index to given value!"""
        index += self.size
        self.data[index] = value
        index >>= 1
        while index:
            self.data[index] = self.func(self.data[2*index], self.data[2*index+1])
            i = index
            self.count[i] = 0
            if self.data[i] == self.data[2 * i]:
                self.count[i] += self.count[2 * i]
            if self.data[i] == self.data[2 * i + 1]:
                self.count[i] += self.count[2 * i + 1]
            index >>= 1


# ------------------- fast io --------------------
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# ------------------- fast io --------------------
n, m = map(int, input().split())
a = list(map(int, input().split()))
st = SegmentTree(a, func=min)
for i in range(m):
    x, y, z = map(int, input().split())
    if x == 1:
        st.update(y,z)
    else:
        print(*st.query(y,z-1))
