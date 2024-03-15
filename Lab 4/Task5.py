def add_edge(adj, src, dest):
    adj[src].append(dest);
    adj[dest].append(src);

def BFS(adj, src, dest, v, pred, dist):
    queue = []
    visited = [False for i in range(v)];
    for i in range(v):
        dist[i] = 1000000
        pred[i] = -1;
    visited[src] = True;
    dist[src] = 0;
    queue.append(src);

    while (len(queue) != 0):
        u = queue[0];
        queue.pop(0);
        for i in range(len(adj[u])):

            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True;
                dist[adj[u][i]] = dist[u] + 1;
                pred[adj[u][i]] = u;
                queue.append(adj[u][i]);
                if (adj[u][i] == dest):
                    return True;

    return False;

def printShortestDistance(adj, s, dest, v):
    pred = [0 for i in range(v)]
    dist = [0 for i in range(v)];

    if (BFS(adj, s, dest, v, pred, dist) == False):
        print("Given source and destination are not connected")
    path = []
    crawl = dest;
    path.append(crawl);

    while (pred[crawl] != -1):
        path.append(pred[crawl]);
        crawl = pred[crawl];

    a = "Time: " + str(dist[dest])

    a += "\nShortest Path: "

    for i in range(len(path) - 1, -1, -1):
        a += f"{path[i]} "

    return a


with open('input5.txt',"r") as file:
    a = list(map(int, file.readline().split()))
    n,m,d = a[0],a[1],a[2]
    adj = [[] for i in range(n)]
    for i in range(n):
        s = list(map(int, file.readline().split()))
        add_edge(adj,s[0],s[1])
    source = 1
    dest = d
    a = printShortestDistance(adj, source, dest, n)
    with open("output5.txt",'w') as file1:
        file1.write(a)


