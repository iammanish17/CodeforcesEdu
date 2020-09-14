# By manish.17, contest: ITMO Academy. СНМ 1, problem: (C) Experience
# https://codeforces.com/profile/manish.17

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [*range(n+1)]
        self.size = [1]*(n+1)
        self.exp = [0]*(n+1)
        self.count = n

    def add(self, a, xp):
        self.exp[self.get(a)] += xp

    def total(self, a):
        ans=self.exp[a]
        while a != self.parent[a]:
            ans += self.exp[self.parent[a]]
            a = self.parent[a]
        return ans

    def get(self, a):
        """Returns the identifier (parent) of the set to which a belongs to!"""
        if self.parent[a] == a:
            return a
        x = a
        while a != self.parent[a]:
            a = self.parent[a]
        #while x != self.parent[x]:
         #   self.parent[x], x = a, self.parent[x]
        return a

    def union(self, a, b):
        """Join two sets that contain a and b!"""
        a, b = self.get(a), self.get(b)
        if a != b:
            if self.size[a] > self.size[b]:
                a, b = b, a
            self.parent[a] = b
            self.size[b] += self.size[a]
            self.exp[a] -= self.exp[b]
            self.count -= 1

    def count_sets(self):
        """Returns the number of disjoint sets!"""
        return self.count

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dsu = DisjointSetUnion(n)

for i in range(m):
    s = input().split()
    if s[0] == "join":
        dsu.union(int(s[1]), int(s[2]))
    elif s[0] == "add":
        dsu.add(int(s[1]), int(s[2]))
    else:
        print(dsu.total(int(s[1])))
