# By manish.17, contest: ITMO Academy. Дерево отрезков часть 1. 2, problem: (A) Segment with the Maximum Sum
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
    def __init__(self, array):
        self.n = len(array)
        self.size = 2**(int(log2(self.n-1))+1) if self.n != 1 else 1
        self.func = lambda a, b: a+b
        self.default = 0
        self.data = [self.default] * (2 * self.size)
        self.pref = [0] * (2 * self.size)
        self.suf = [0] * (2 * self.size)
        self.seg = [0] * (2 * self.size)
        self.process(array)

    def process(self, array):
        self.data[self.size : self.size + self.n] = array
        for i in range(n):
            j = i + self.size
            self.seg[j] = self.pref[j] = self.suf[j] = max(array[i],0)
        for i in range(self.size-1, -1, -1):
            self.data[i] = self.func(self.data[2*i], self.data[2*i+1])
            self.pref[i] = max(self.pref[2*i], self.data[2*i] + self.pref[2*i+1])
            self.suf[i] = max(self.suf[2*i+1], self.data[2*i+1] + self.suf[2*i])
            self.seg[i] = max(self.seg[2*i], self.seg[2*i + 1], self.suf[2*i] + self.pref[2*i+1])

    def update(self, index, value):
        """Updates the element at index to given value!"""
        index += self.size
        self.data[index] = value
        self.pref[index] = max(value,0)
        self.suf[index] = max(value,0)
        self.seg[index] = max(value,0)
        index >>= 1
        while index:
            self.data[index] = self.func(self.data[2*index], self.data[2*index+1])
            i = index
            self.pref[i] = max(self.pref[2 * i], self.data[2 * i] + self.pref[2 * i + 1])
            self.suf[i] = max(self.suf[2 * i + 1], self.data[2 * i + 1] + self.suf[2 * i])
            self.seg[i] = max(self.seg[2 * i], self.seg[2 * i + 1], self.suf[2 * i] + self.pref[2 * i + 1])
            index >>= 1


n, m = map(int, input().split())
a = list(map(int, input().split()))
st = SegmentTree(a)
print(st.seg[1])
for i in range(m):
    x, y = map(int, input().split())
    st.update(x, y)
    print(st.seg[1])
