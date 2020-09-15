# By manish.17, contest: ITMO Academy. СНМ 2, problem: (C) Restructuring Company
# https://codeforces.com/profile/manish.17

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [*range(n+1)]
        self.size = [1]*(n+1)
        self.max = [*range(n+1)]

    def get(self, a):
        """Returns the identifier (parent) of the set to which a belongs to!"""
        if self.parent[a] == a:
            return a
        x = a
        while a != self.parent[a]:
            a = self.parent[a]
        while x != self.parent[x]:
            self.parent[x], x = a, self.parent[x]
        return a

    def union(self, a, b):
        """Join two sets that contain a and b!"""
        a, b = self.get(a), self.get(b)
        if a != b:
            if self.size[a] > self.size[b]:
                a, b = b, a
            self.parent[a] = b
            self.size[b] += self.size[a]
            self.max[b] = max(self.max[a], self.max[b])

    def count_sets(self):
        """Returns the number of disjoint sets!"""
        return self.count

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
dsu = DisjointSetUnion(n)
dsu2 = DisjointSetUnion(n)

for i in range(q):
    x, y, z = map(int, input().split())
    if x == 1:
        dsu.union(y, z)
    if x == 2:
        p = dsu2.max[dsu2.get(y)]
        while p < z:
            dsu.union(p, z)
            dsu2.union(p, p+1)
            p = dsu2.max[dsu2.get(p + 1)]
        dsu2.union(y, z)
    if x == 3:
        print("YES" if dsu.get(y) == dsu.get(z) else "NO")
