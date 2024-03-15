def matrix(arr,n):
    arr1 = []
    for i in range(n+1):
        arr1.append([0]*(n+1))

    for i in arr:
        arr1[i[0]][i[1]] = i[2]

    return arr1

with open("input1.txt","r") as file:
    a = list(map(int, file.readline().split()))
    n = int(a[0])
    m = int(a[1])
    arr = []
    for i in range(m):
        arr.append(list(map(int, file.readline().split())))
    arr1 = matrix(arr,n)
    with open("output1(A).txt","w") as file1:
        for i in arr1:
            a = str(i).replace(",", "")
            file1.write(str(a[1:-1:])+'\n')