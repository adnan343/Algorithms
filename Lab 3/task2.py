def max(list1, list2):
    if list1>list2:
        max1=list1
    else:
        max1=list2
    return max1

def devide(list1):
    if len(list1)<=1:
        return list1
    mid=len(list1)//2
    list2=list1[:mid:]
    list3=list1[mid::]
    if len(list2)!=1:
        list2=devide(list2)
    if len(list3)!=1:
        list3=devide(list3)
    return max(list2,list3)


with open("input2.txt","r") as file:
    file.readline()
    arr=list(map(int,file.readline().split()))
    a=devide(arr)
    with open("output2.txt","w") as file1:
        file1.write(str(a[0]))
