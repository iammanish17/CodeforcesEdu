# By manish.17, contest: ITMO Academy. Дерево отрезков часть 1. 4, problem: (B) Cryptography
# https://codeforces.com/profile/manish.17

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
from math import inf, log2


class SegmentTree:
    def __init__(self, array, mod):
        self.n = len(array)
        self.mod = mod
        self.size = 2**(int(log2(self.n-1))+1) if self.n != 1 else 1
        self.func = lambda a,b:[(a[0]*b[0]+a[1]*b[2]) % self.mod,
                                (a[0]*b[1]+a[1]*b[3]) % self.mod,
                                (a[2]*b[0]+a[3]*b[2]) % self.mod,
                                (a[2]*b[1]+a[3]*b[3]) % self.mod]
        self.default = [1, 0, 0, 1]
        self.data = [[0,0,0,0]] * (2 * self.size)
        self.process(array)

    def process(self, array):
        self.data[self.size : self.size+self.n] = array
        for i in range(self.size-1, -1, -1):
            self.data[i] = self.func(self.data[2*i], self.data[2*i+1])

    def query(self, alpha, omega):
        """Returns the result of function over the range (inclusive)!"""
        if alpha == omega:
            return self.data[alpha + self.size]
        alpha += self.size
        omega += self.size + 1
        results = []
        res = self.default
        while alpha < omega:
            res2 = self.default
            if alpha & 1:
                res = self.func(res, self.data[alpha])
                alpha += 1
            if omega & 1:
                omega -= 1
                res2 = self.func(res2, self.data[omega])
            alpha >>= 1
            omega >>= 1
            results += [res2]
        results = results[::-1]
        for i in results: res = self.func(res, i)
        return res

r, n, m = map(int, input().split())
matrices = []
for i in range(n):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    e = input()
    matrices += [[a, b, c, d]]

st = SegmentTree(matrices, r)
for i in range(m):
    l, r = map(int, input().split())
    result = st.query(l-1, r-1)
    print(result[0], result[1])
    print(result[2], result[3])
    print("")
