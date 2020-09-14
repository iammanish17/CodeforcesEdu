# By manish.17, contest: ITMO Academy. СНМ 1, problem: (D) Cutting a graph
# https://codeforces.com/profile/manish.17

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [*range(n+1)]
        self.size = [1]*(n+1)
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
            self.count -= 1

    def count_sets(self):
        """Returns the number of disjoint sets!"""
        return self.count

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
for i in range(m):input()

dsu = DisjointSetUnion(n)

ans = []

queries = []
for i in range(k):queries += [input().split()]

for s in queries[::-1]:
    if s[0] == "cut":
        dsu.union(int(s[1]), int(s[2]))
    else:
        g1, g2 = dsu.get(int(s[1])), dsu.get(int(s[2]))
        ans += ["YES" if g1==g2 else "NO"]

print("\n".join(ans[::-1]))
