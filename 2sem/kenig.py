def bipartite(graph):
    n = len(graph.keys())
    colors = [-1] * n

    for start in range(n):
        if colors[start] == -1:
            queue = [start]
            colors[start] = 0

            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    # Если сосед уже окрашен в тот же цвет, граф не двудольный
                    elif colors[v] == colors[u]:
                        return False, []

    set1 = [i for i in range(n) if colors[i] == 0]
    set2 = [i for i in range(n) if colors[i] == 1]

    return True, (set1, set2)


def kuhn(graph):
    n = len(graph.keys())
    match = [-1] * n
    visited = [False] * n
    fl, parts = bipartite(graph)
    if not fl:
        return -1

    L = parts[0]

    def dfs(v):
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                if match[u] == -1 or dfs(match[u]):
                    match[u] = v
                    return True
        return False

    max_matching = 0
    for v in L:
        visited = [False] * n
        if dfs(v):
            max_matching += 1
    return match


G = {}
G[0] = [1, 3, 5]
G[1] = [0, 2, 6]
G[2] = [1]
G[3] = [0, 4]
G[4] = [3, 5, 7]
G[5] = [0, 4]
G[6] = [1]
G[7] = [4]
n = 7

mt = kuhn(G)
fl, parts = bipartite(G)
if not fl:
    exit(0)

g = {}

for v in range(n + 1):
    g[v] = []

free = []

for v in parts[1]:
    if mt[v] != -1:
        g[mt[v]].append(v)
        for u in G[v]:
            if u != mt[v]:
                g[v].append(u)
    else:
        free.append(v)
        for u in G[v]:
            g[v].append(u)

l = []
r = []

used = [False] * (n + 1)

def dfs(v, c):
    if c == 0:
        l.append(v)
    else:
        r.append(v)
    used[v] = True
    for u in g[v]:
        if not used[u]:
            dfs(u, c ^ 1)

for u in free:
    dfs(u, 0)

l_ = [1] * (n + 1)
for v in l:
    l_[v] = -1

ans = len(r)
for v in parts[1]:
    if l_[v] == 1:
        ans += 1

print(ans)
for v in parts[1]:
    if l_[v] == 1:
        print(v, end=' ')
for v in r:
    print(v, end=' ')