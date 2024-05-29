import heapq


def dijkstra(adj, root, n):
    visited = [0] * (n + 1)
    dist = [float('inf')] * (n + 1)
    dist[root] = 0
    queue = []
    heapq.heappush(queue, (0, root))
    while len(queue) > 0:
        index = heapq.heappop(queue)[1]
        for i in adj[index]:
            if visited[i[0]] == 0:
                if dist[i[0]] > dist[index] + i[1]:
                    dist[i[0]] = dist[index] + i[1]
                    heapq.heappush(queue, (i[1], i[0]))
    return dist


def adjList(n, arr):
    adj = [0] * (n + 1)
    for i in arr:
        if adj[i[0]] == 0:
            adj[i[0]] = [(i[1], i[2])]
        else:
            adj[i[0]].append((i[1], i[2]))
    for i in range(1, len(adj)):
        if adj[i] == 0:
            adj[i] = [(0, float('inf'))]
    return adj


with open("input1.txt", "r") as file:
    a = list(map(int, file.readline().split()))
    n, m = a[0], a[1]
    arr = []
    for i in range(m):
        arr.append(list(map(int, file.readline().split())))
    # print(arr)
    root = int(file.readline().strip())
    # print(root)
    adj = adjList(n, arr)
    # print(adj)
    dist = dijkstra(adj, root, n)
    res = []
    for i in range(1, len(dist)):
        if dist[i] == float('inf'):
            res.append(-1)
        else:
            res.append(dist[i])
    # print(res)
    with open("output1.txt", "w") as file2:
        res = ' '.join(map(str, res))
        file2.write(res)
