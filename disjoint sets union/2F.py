# By manish.17, contest: ITMO Academy. СНМ 2, problem: (F) Dense spanning tree
# https://codeforces.com/profile/manish.17

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [*range(n+1)]
        self.size = [1]*(n+1)

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


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
y = []
for _ in range(m):
    b, e, w = map(int, input().split())
    y += [[w, b, e]]

y = sorted(y, key=lambda x: x[0])
ans = 10**18
found = False
for i in range(len(y)):
    dsu = DisjointSetUnion(n)
    cnt = 0
    m1 = 10**18
    m2 = -10**18
    for j in range(i, len(y)):
        p, q, r = y[j]
        if dsu.get(q) != dsu.get(r):
            dsu.union(q, r)
            cnt += 1
            m1 = min(m1, p)
            m2 = max(m2, p)
            if cnt == n-1:break
    if cnt == n-1:
        found = True
        ans = min(ans, m2-m1)
    else:break

if not found:
    print("NO")
else:
    print("YES")
    print(ans)
