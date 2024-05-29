def adjList(arr, n):
    arr1 = [0] * (n + 1)
    for i in arr:
        if arr1[i[0]] == 0:
            arr1[i[0]] = [(i[1])]
        else:
            arr1[i[0]].append((i[1]))
    for i in range(len(arr1)):
        if arr1[i] == 0:
            arr1[i] = [0]
    return arr1


def inDegrees(adjList):
    inDegrees = [0] * len(adjList)
    for i in adjList:
        if i != 0:
            for j in i:
                inDegrees[j] += 1
    return inDegrees


def dfs(root, adjList, stack, visited):
    visited[root] = True
    if adjList[root] != 0:
        for i in adjList[root]:
            if not visited[i]:
                dfs(i, adjList, stack, visited)
    stack.append(root)
    return stack


def tropoSort(adjList):
    stack = []
    visited = [False] * len(adjList)
    indegrees = inDegrees(adjList)
    for i in range(len(indegrees)):
        if indegrees[i] == 0:
            stack = dfs(i, adjList, stack, visited)
    result = ''
    if len(stack) == len(indegrees):
        for i in range(len(stack) - 1, 0, -1):
            result += str(stack[i]) + " "
    else:
        result = "IMPOSSIBLE"
    return result


with open("input1.txt", "r") as file:
    a = list(map(int, file.readline().split()))
    n = a[0]
    m = a[1]
    arr = []
    for i in range(m):
        arr.append(list(map(int, file.readline().split())))
    # print(arr)
    adjList = adjList(arr, n)
    # print(adjList)
    result = tropoSort(adjList)
    with open("output1(B).txt", "w") as file1:
        file1.write(result)
