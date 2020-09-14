# By manish.17, contest: ITMO Academy. СНМ 2, problem: (D) Bosses
# https://codeforces.com/profile/manish.17

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [*range(n+1)]
        self.num = [0]*(n+1)
        self.count = n

    def get(self, a, query=False):
        """Returns the identifier (parent) of the set to which a belongs to!"""
        if self.parent[a] == a:
            return a if not query else 0
        x = a
        ans = 0
        di = {}
        while a != self.parent[a]:
            di[a] = ans
            ans += self.num[a]
            a = self.parent[a]
        while x != self.parent[x]:
            self.num[x] = ans - di[x]
            self.parent[x], x = a, self.parent[x]
        return a if not query else ans

    def union(self, a, b):
        """Join two sets that contain a and b!"""
        a, b = self.get(a), self.get(b)
        if a != b:
            self.parent[a] = b
            self.num[a] += 1
            self.count -= 1

    def count_sets(self):
        """Returns the number of disjoint sets!"""
        return self.count

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dsu = DisjointSetUnion(n)
for i in range(m):
    s = [int(k) for k in input().split()]
    if s[0] == 1:
        dsu.union(s[1], s[2])
    else:
        print(dsu.get(s[1], query=True))
