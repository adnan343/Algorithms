def adjList(arr,n):
    arr1 = [0]*(n+1)
    for i in arr:
        if arr1[i[0]] == 0:
            arr1[i[0]] = [(i[1],i[2])]
        else:
            arr1[i[0]].append((i[1],i[2]))

    return arr1

with open("input1.txt","r") as file:
    a = list(map(int, file.readline().split()))
    n = int(a[0])
    m = int(a[1])
    arr = []
    for i in range(m):
        arr.append(list(map(int, file.readline().split())))
    arr1 = adjList(arr,n)
    with open("output1(B).txt","w") as file1:
        for i in range(len(arr1)):
            if arr1[i] != 0:
                a = f"{i} : {arr1[i]}\n"
                a = a.replace("[","").replace("]","").replace("),",")")
            else:
                a = f"{i} :\n"
            file1.write(a)