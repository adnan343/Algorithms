def amIFree(arr):
    count=0
    arr1=[]
    endTime=0
    for i in arr:
        if i[0]>=endTime:
            endTime=i[1]
            count+=1
            arr1.append(i)
    str1=str(count)
    for i in arr1:
        str1+=f"\n{i[0]} {i[1]}"
    with open("task3out.txt", "w") as file1:
        file1.write(str1)

def sorter(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

with open("task3in.txt", "r") as file:
    n=file.readline()
    list1=[]
    for i in range(int(n)):
        temp=[]
        a=file.readline().strip().split()
        temp.append(int(a[0]))
        temp.append(int(a[-1]))
        list1.append(temp)
    list1=sorter(list1)
    amIFree(list1)