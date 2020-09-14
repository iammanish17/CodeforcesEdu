# By manish.17, contest: ITMO Academy. СНМ 2, problem: (E) Spanning Tree
# https://codeforces.com/profile/manish.17

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [*range(n+1)]
        self.size = [1]*(n+1)
        self.min, self.max = [*range(n+1)], [*range(n+1)]
        self.count = n

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
            self.min[b] = min(self.min[a], self.min[b])
            self.max[b] = max(self.max[a], self.max[b])
            self.count -= 1

    def count_sets(self):
        """Returns the number of disjoint sets!"""
        return self.count

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dsu = DisjointSetUnion(n)
di = {}
for _ in range(m):
    b, e, w = map(int, input().split())
    if w not in di:
        di[w] = []
    di[w] += [[b, e]]

x = sorted([k for k in di])
ans = 0
for i in x:
    for p, q in di[i]:
        if dsu.get(p) != dsu.get(q):
            dsu.union(p, q)
            ans += i
print(ans)
