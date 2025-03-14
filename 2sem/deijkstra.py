class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        self.build_heap()

    def left(self, i):
        if (2 * i + 1) < self.size:
            return self.arr[2 * i + 1]
        else:
            return None

    def right(self, i):
        if (2 * i + 2) < self.size:
            return self.arr[2 * i + 2]
        else:
            return None

    def parent(self, i):
        if (i - 1) // 2 < 0:
            return None
        return self.arr[(i - 1) // 2]

    def SiftDown(self, i):
        j = i
        left = self.left(i)
        right = self.right(i)

        if left and left[0] < self.arr[j][0]:
            j = 2 * i + 1
        if right and right[0] < self.arr[j][0]:
            j = 2 * i + 2

        if j != i:
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            self.SiftDown(j)

    def SiftUp(self, i):
        parent = self.parent(i)
        if not parent:
            return
        if self.arr[i][0] < parent[0]:
            self.arr[i], self.arr[(i - 1) // 2] = self.arr[(i - 1) // 2], self.arr[i]
            self.SiftUp((i - 1) // 2)

    def build_heap(self):
        for i in range(self.size - 1, -1, -1):
            self.SiftDown(i)

    def get_min(self):
        return self.arr[0]

    def delet(self):
        last_value = self.arr.pop()
        self.size -= 1
        if self.size > 0:
            self.arr[0] = last_value
            self.SiftDown(0)

    def push(self, a):
        self.size += 1
        self.arr.append(a)
        self.SiftUp(self.size - 1)

def Dijkstra(G,s):
    V = len(G.keys()) + 1
    dist = [float('inf') for i in range(V)]
    prev = [None for i in range(V)]
    dist[s] = 0
    S = Heap([])
    S.push([0, s])
    while len(S.arr) > 0:
        p = S.get_min()
        S.delet()
        d, v = p[0], p[1]
        for u, w in G[v]:
            if dist[u] > d + w:
                dist[u] = d + w
                prev[u] = v
                S.push([dist[u], u])
    return dist, prev

G = {}
G[1] = [[2, 2], [3, 4], [5, 100]]
G[2] = [[1, 2], [3, 1], [4, 5]]
G[3] = []
G[4] = [[2, 5], [5, 2]]
G[5] = [[4, 2]]

dist, prev = Dijkstra(G,1)
print(dist)