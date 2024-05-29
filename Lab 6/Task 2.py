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


with open("input2.txt", "r") as file:
    a = list(map(int, file.readline().split()))
    n, m = a[0], a[1]
    arr = []
    for i in range(m):
        arr.append(list(map(int, file.readline().split())))
    # print(arr)
    b = list(map(int, file.readline().split()))
    root1, root2 = b[0], b[1]
    # print(root1, root2)
    adj = adjList(n, arr)
    # print(adj)
    dist1 = dijkstra(adj, root1, n)
    # print(dist1)
    dist2 = dijkstra(adj, root2, n)
    # print(dist2)
    time = float('inf')
    for i in range(len(dist1)):
        if max(dist1[i], dist2[i]) < time:
            time = max(dist1[i], dist2[i])
            point = i
    if time == float('inf'):
        s = "Impossible"
    else:
        s = f"Time {time}\nNode {point}"

    with open("output2.txt", "w") as file2:
        file2.write(s)
