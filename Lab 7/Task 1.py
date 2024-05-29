def make_friend(parent, size, u, v):
    paru = find(parent, u)
    parv = find(parent, v)
    # print(paru,parv)
    if paru != parv:
        t = size[paru]
        parent[paru] = parv
        size[parv] = t + size[parv]
    return size[parv]


def find(parent, u):
    par = parent[u]
    if parent[u] != u:
        par = find(parent, parent[u])
    return par


with open("input1.txt", "r") as file:
    a = list(map(int, file.readline().split()))
    n = a[0]
    k = a[1]
    edge = []
    for i in range(k):
        edge.append(list(map(int, file.readline().split())))

    parent = [0] * n
    for i in range(n):
        parent[i] = i
    size = [1] * n
    result = ""
    for i, j in edge:
        arr = make_friend(parent, size, i, j)
        result += str(arr)
        result += '\n'

    with open("output1.txt", "w") as file1:
        file1.write(result)
