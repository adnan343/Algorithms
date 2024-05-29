


def find(par, r):
    if par[r] == r:
        return r
    par[r] = find(par, par[r])
    return par[r]


def union(par, rank, i, j):
    rep_i = find(par, i)
    rep_j = find(par, j)
    if rep_i == rep_j:
        return False
    if rep_i != rep_j:
        if rank[rep_i] < rank[rep_j]:
            par[rep_i] = rep_j
        else:
            par[rep_j] = rep_i
            rank[rep_i] += rank[rep_j]
    return True

with open("input2.txt", "r") as file:
    x = file.readline()
    x = x.split()
    v = int(x[0]) + 1
    e = int(x[1])
    parent = [i for i in range(v)]
    child = [1 for i in range(v)]
    graph = []

    for i in range(e):
        var = file.readline()
        var = var.split()
        var = [int(i) for i in var]
        graph.append(var)


    for i in range(len(graph)):
        for j in range(len(graph) - i - 1):
            if graph[j][2] > graph[j + 1][2]:
                graph[j], graph[j + 1] = graph[j + 1], graph[j]

    lowest_cost = 0
    for k in graph:
        u, v, w = k
        if union(parent, child, u - 1, v - 1):
            lowest_cost += w
    with open("output2.txt", "w") as file1:
        file1.write(str(lowest_cost))