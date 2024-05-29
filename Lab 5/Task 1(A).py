def adjList(arr, n):
    arr1 = [0] * (n + 1)
    for i in arr:
        if arr1[i[0]] == 0:
            arr1[i[0]] = [(i[1])]
        else:
            arr1[i[0]].append((i[1]))
    return arr1


def inDegrees(adjList):
    inDegrees = [0] * len(adjList)
    for i in adjList:
        if i != 0:
            for j in i:
                inDegrees[j] += 1
    return inDegrees


def tropoSort(adjList):
    inDegrees1 = inDegrees(adjList)
    q = []
    for i in range(len(inDegrees1)):
        if inDegrees1[i] == 0:
            q.append(i)
    cNode = q.pop(0)
    result = [cNode]
    if adjList[cNode] != 0:
        for i in adjList[cNode]:
            inDegrees1[i] -= 1
        print(inDegrees1)
    while len(q) != 0:
        cNode = q.pop(0)
        result.append(cNode)
        # print(cNode)
        if adjList[cNode] != 0:
            for i in adjList[cNode]:
                inDegrees1[i] -= 1
            # print(inDegrees1)
        for i in range(len(inDegrees1)):
            if inDegrees1[i] == 0 and i not in q and i not in result:
                q.append(i)
    if len(result) == len(adjList):
        return result
    else:
        return "IMPOSSIBLE"


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
    # print(inDegrees(adjList))
    result = tropoSort(adjList)
    with open("output1(A).txt", "w") as file1:
        if result != "IMPOSSIBLE":
            for i in range(1, len(result)):
                file1.write(str(result[i]) + " ")
        else:
            file1.write(result)
