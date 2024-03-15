def adjList(arr,n):
    arr1 = [0]*(n+1)
    for i in arr:
        if arr1[i[0]] == 0:
            arr1[i[0]] = [i[1]]
        else:
            arr1[i[0]].append(i[1])
        if arr1[i[1]] == 0:
            arr1[i[1]] = [i[0]]
        else:
            arr1[i[1]].append(i[0])

    return arr1

def bfs(arr1):
    color = [0]*(len(arr1)+1)
    queue = []
    result = []
    color[1] = 1
    queue.append(1)
    result.append(1)
    while len(queue) > 0:
        temp = queue.pop(0)
        for i in arr1[temp]:
            if color[i] == 0:
                queue.append(i)
                color[i] = 1
                result.append(i)
    return result

with open("input2.txt","r") as file:
    a = list(map(int, file.readline().split()))
    n = int(a[0])
    m = int(a[1])
    arr = []
    for i in range(m):
        arr.append(list(map(int, file.readline().split())))
    # print(arr)
    arr1 = adjList(arr,n)
    # print(arr1)
    arr2 = bfs(arr1)
    with open("output2.txt","w") as file1:
        a = str(arr2).replace(",", "").replace("[", "").replace("]",'')
        file1.write(a)