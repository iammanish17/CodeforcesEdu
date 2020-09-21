# By manish.17, contest: ITMO Academy. Дерево отрезков 2 - 2, problem: (B) Multiplication and Sum
# https://codeforces.com/profile/manish.17

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

from math import inf, log2


class LazySegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.size = 2 ** (int(log2(self.n - 1)) + 1) if self.n != 1 else 1
        self.default = 0
        self.mod = 10**9 + 7
        self.data = [self.default] * (2 * self.size)
        self.lazy = [1] * (2 * self.size)
        self.process(array)

    def process(self, array):
        self.data[self.size: self.size + self.n] = array
        for i in range(self.size - 1, -1, -1):
            self.data[i] = (self.data[2 * i] + self.data[2 * i + 1]) % self.mod

    def push(self, index):
        """Push the information of the root to it's children!"""
        self.lazy[2 * index] = (self.lazy[2*index]*self.lazy[index]) % self.mod
        self.lazy[2 * index + 1] = (self.lazy[2*index + 1]* self.lazy[index]) % self.mod
        self.data[2 * index] = (self.data[2*index]* self.lazy[index]) % self.mod
        self.data[2 * index + 1] = (self.data[2*index + 1]* self.lazy[index]) % self.mod
        self.lazy[index] = 1

    def build(self, index):
        """Build data with the new changes!"""
        index >>= 1
        while index:
            self.data[index] = ((self.data[2 * index] + self.data[2 * index + 1])*
                                self.lazy[index]) % self.mod
            index >>= 1

    def query(self, alpha, omega):
        """Returns the result of function over the range (inclusive)!"""
        res = self.default
        alpha += self.size
        omega += self.size + 1
        for i in range(len(bin(alpha)[2:]) - 1, 0, -1):
            self.push(alpha >> i)
        for i in range(len(bin(omega - 1)[2:]) - 1, 0, -1):
            self.push((omega - 1) >> i)
        while alpha < omega:
            if alpha & 1:
                res = (res+self.data[alpha]) % self.mod
                alpha += 1
            if omega & 1:
                omega -= 1
                res = (res + self.data[omega]) % self.mod
            alpha >>= 1
            omega >>= 1
        return res

    def update(self, alpha, omega, value):
        """Increases all elements in the range (inclusive) by given value!"""
        alpha += self.size
        omega += self.size + 1
        l, r = alpha, omega
        while alpha < omega:
            if alpha & 1:
                self.data[alpha] = (self.data[alpha]*value) % self.mod
                self.lazy[alpha] = (self.lazy[alpha]*value) % self.mod
                alpha += 1
            if omega & 1:
                omega -= 1
                self.data[omega] = (self.data[omega]*value) % self.mod
                self.lazy[omega] = (self.lazy[omega]*value) % self.mod
            alpha >>= 1
            omega >>= 1
        self.build(l)
        self.build(r - 1)

n, m = map(int, input().split())
st = LazySegmentTree([1]*n)
for _ in range(m):
    a = list(map(int, input().split()))
    if a[0] == 1:
        st.update(a[1], a[2]-1, a[3])
    else:
        print(st.query(a[1], a[2]-1))
