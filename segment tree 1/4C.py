# By manish.17, contest: ITMO Academy. Дерево отрезков часть 1. 4, problem: (C) Number of Inversions on Segment
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
        self.data = [0] * (2 * self.size)
        self.pref = [[0]*(2*self.size) for i in range(40)]
        self.process(array)

    def count(self, l, r):
        ans = 0
        for i in range(1, 40):
            x = 0
            for j in range(i-1, -1, -1):
                x += self.pref[j][r]
            ans += self.pref[i][l] * x
        return ans

    def process(self, array):
        for i in range(self.n):
            self.pref[array[i] - 1][self.size + i] = 1
        for i in range(self.size-1, -1, -1):
            for j in range(40):
                self.pref[j][i] = self.pref[j][2*i] + self.pref[j][2*i+1]
            self.data[i] = self.data[2*i] + self.data[2*i + 1] + self.count(2*i, 2*i+1)

    def query(self, alpha, omega):
        """Returns the result of function over the range (inclusive)!"""
        if alpha == omega:
            return self.data[alpha + self.size]
        segment1 = []
        segment2 = []
        alpha += self.size
        omega += self.size + 1
        a,o = alpha, omega
        while alpha < omega:
            if alpha & 1:
                segment1.append(alpha)
                alpha += 1
            if omega & 1:
                omega -= 1
                segment2.append(omega)
            alpha >>= 1
            omega >>= 1
        segment = segment1 + segment2[::-1]
        if len(segment) == 1: return self.data[segment[0]]
        pref = [self.pref[i][segment[0]] for i in range(40)]
        ans = self.data[segment[0]]
        for ind in range(1, len(segment)):
            ans += self.data[segment[ind]]
            for i in range(1, 40):
                x = 0
                for j in range(i - 1, -1, -1):
                    x += self.pref[j][segment[ind]]
                ans += pref[i] * x
            for i in range(40):
                pref[i] += self.pref[i][segment[ind]]
        return ans

    def update(self, index, value, old):
        """Updates the element at index to given value!"""
        index += self.size
        self.pref[value-1][index] += 1
        self.pref[old-1][index] -= 1
        index >>= 1
        while index:
            i = index
            self.pref[value-1][index] += 1
            self.pref[old-1][index] -= 1
            for j in range(40):
                self.pref[j][i] = self.pref[j][2*i] + self.pref[j][2*i+1]
            self.data[i] = self.data[2 * i] + self.data[2 * i + 1] + self.count(2 * i, 2 * i + 1)
            index >>= 1

n, q = map(int, input().split())
a = list(map(int, input().split()))
st = SegmentTree(a)
for _ in range(q):
    x, y, z = map(int, input().split())
    if x == 1:
        print(st.query(y-1, z-1))
    else:
        st.update(y - 1, z, a[y-1])
        a[y-1] = z
