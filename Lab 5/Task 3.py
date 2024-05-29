def adjList(arr, n):
    arr1 = [0] * (n + 1)
    arr2 = [0] * (n + 1)
    for i in arr:
        if arr1[i[0]] == 0:
            arr1[i[0]] = [(i[1])]
        else:
            arr1[i[0]].append((i[1]))
        if arr2[i[1]] == 0:
            arr2[i[1]] = [(i[0])]
        else:
            arr2[i[1]].append((i[0]))
    for i in range(len(arr1)):
        if arr1[i] == 0:
            arr1[i] = [0]
        if arr2[i] == 0:
            arr2[i] = [0]
    return arr1, arr2


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
    # indegrees = inDegrees(adjList)
    # print(indegrees)
    for i in range(len(visited)):
        if not visited[i]:
            stack = dfs(i, adjList, stack, visited)
    # print(stack)
    result = []
    # if len(stack) == len(indegrees):
    for i in range(len(stack) - 1, 0, -1):
        result.append(stack[i])
    # else:
    #     result = "IMPOSSIBLE"
    return result


def scc(tAdjList, tropoList):
    visited = [False] * (len(tropoList) + 1)
    finalResult = []
    comp = []
    for i in tropoList:
        if not visited[i]:
            comp = dfs(i, tAdjList, comp, visited)
            # print(comp)
            finalResult.append(comp)
            comp = []
    return finalResult


with open("input3.txt", "r") as file:
    a = list(map(int, file.readline().split()))
    n = a[0]
    m = a[1]
    arr = []
    for i in range(m):
        arr.append(list(map(int, file.readline().split())))
    # print(arr)
    adjList, tAdjList = adjList(arr, n)
    # print(adjList)
    result = tropoSort(adjList)
    # print(result)
    finalResult = scc(tAdjList, result)
    # print(finalResult)
    with open("output3.txt", "w") as file:
        for i in finalResult:
            i.sort()
            for j in i:
                if j != 0:
                    file.write(str(j) + " ")
            file.write("\n")
