def sorter(array1,array2):
    narray=array1+array2
    narray.sort()
    narray=str(narray)
    narray=narray[1:-1]
    narray=narray.replace(",","")
    return narray

with open("task2in.txt", "r") as file:
    file.readline()
    arr1 = list(map(int,file.readline().split()))
    file.readline()
    arr2 = list(map(int,file.readline().split()))
    with open("task2outnlogn.txt", "w") as file1:
        file1.write(sorter(arr1, arr2))