# By manish.17, contest: ITMO Academy. СНМ 2, problem: (A) People are leaving
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

n, m = map(int, input().split())
dsu = DisjointSetUnion(n)

last = False

for i in range(m):
    s = input().split()
    if s[0] == "-":
        if int(s[1]) != n:
            dsu.union(int(s[1]), int(s[1])+1)
        else:
            last = True
    else:
        g = dsu.max[dsu.get(int(s[1]))]
        if g == n:
            print(-1 if last else n)
        else:
            print(g)
