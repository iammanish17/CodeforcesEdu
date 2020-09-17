# By manish.17, contest: ITMO Academy. Дерево отрезков часть 1. 3, problem: (E) Addition to Segment
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
            res += self.data[index]
            index >>= 1
        return res

    def update(self, alpha, omega, value):
        """Increases all elements in the range (inclusive) by given value!"""
        alpha += self.size
        omega += self.size + 1
        while alpha < omega:
            if alpha & 1:
                self.data[alpha] += value
                alpha += 1
            if omega & 1:
                omega -= 1
                self.data[omega] += value
            alpha >>= 1
            omega >>= 1

n, m = map(int, input().split())
st = SegmentTree([0]*n)

for i in range(m):
    a = list(map(int, input().split()))
    if len(a) == 4:
        st.update(a[1], a[2]-1, a[3])
    else:
        print(st.query(a[1]))
