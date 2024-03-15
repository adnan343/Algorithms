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

def dfs(arr1,color,result,u=1):
    color[u] = 1
    result.append(u)
    for i in arr1[u]:
        if color[i] == 0:
            dfs(arr1,color,result,i) 
    return result


with open("input3.txt","r") as file:
    a = list(map(int, file.readline().split()))
    n = int(a[0])
    m = int(a[1])
    arr = []
    for i in range(m):
        arr.append(list(map(int, file.readline().split())))
    # print(arr)
    arr1 = adjList(arr,n)
    # print(arr1)
    color = [0]*(len(arr1)+1)
    result = []
    arr2 = dfs(arr1,color,result)
    with open("output3.txt","w") as file1:
        a = str(arr2).replace(",", "").replace("[", "").replace("]",'')
        file1.write(a)