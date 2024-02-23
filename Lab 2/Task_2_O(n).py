def sorter(arr1, arr2):
    arr = []
    i = 0
    j = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1

        else:
            arr.append(arr2[j])
            #print(arr)
            j += 1

    if i == len(arr1):
        arr += arr2[j:]
    else:
        arr += arr1[i:]

    narray = str(arr)
    narray = narray[1:-1]
    narray = narray.replace(",", "")
    return narray


with open("task2in.txt", "r") as file:
    file.readline()
    arr1 = list(map(int,file.readline().split()))
    file.readline()
    arr2 = list(map(int,file.readline().split()))
    with open("task2outn.txt", "w") as file1:
        file1.write(sorter(arr1, arr2))