def sorter(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def counter(arr,m):
    count=0
    endTime=[0]*m
    for i in arr:
        for j in range(m):
            if i[0]>=endTime[j]:
                endTime[j]=i[1]
                count+=1
                break
    str1=str(count)
    with open("task4out.txt", "w") as file1:
        file1.write(str1)


with open("task4in.txt", "r") as file:
    n=file.readline().strip().split()
    list1=[]
    for i in range(int(n[0])):
        temp=[]
        a=file.readline().strip().split()
        temp.append(int(a[0]))
        temp.append(int(a[-1]))
        list1.append(temp)
    list1=sorter(list1)
    counter(list1,int(n[1]))