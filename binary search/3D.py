# By manish.17, contest: ITMO Academy. Двоичный поиск - 3, problem: (D) Minimum maximum on the Path
# https://codeforces.com/profile/manish.17

from collections import deque
def bfs(graph, alpha=0):
    """Breadth first search on a graph!"""
    n = len(graph)
    q = deque([alpha])
    used = [False]*n
    used[alpha] = True
    dist, parents = [0]*n, [-1]*n
    while q:
        v = q.popleft()
        for u in graph[v]:
            if not used[u]:
                used[u] = True
                q.append(u)
                dist[u] = dist[v] + 1
                parents[u] = v
    return used, dist, parents


n, m, d = map(int, input().split())
x = []
for i in range(m):
    a, b, w = map(int, input().split())
    x += [[w, a, b]]

alpha, omega = 0, 10**16
while alpha < omega:
    mid = (alpha + omega) // 2
    graph = [[] for __ in range(n+1)]
    for w, a, b in x:
        if w <= mid:
            graph[a] += [b]
    used, dist, parents = bfs(graph, 1)
    if 0 < dist[n] <= d:
        omega = mid
    else:
        alpha = mid + 1

graph = [[] for __ in range(n+1)]
for w, a, b in x:
    if w <= omega:
        graph[a] += [b]

used, dist, parents = bfs(graph, 1)
path = [n]
v = n
while parents[v] != -1:
    path += [parents[v]]
    v = parents[v]

if len(path) > d+1:
    print(-1)
    quit()
print(len(path) - 1)
print(*path[::-1])
