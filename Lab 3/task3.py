def merge(list1, list2, count):
    list3=[]
    i,j=0,0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i+=1
        else:
            count += len(list1)-1 - i + 1
            list3.append(list2[j])
            j+=1

    if i < len(list1):
        list3.extend(list1[i:])
    elif j < len(list2):
        list3.extend(list2[j:])
    return (list3,count)


def merge_sort(list1,count=0):
    if len(list1)<=1:
        return list1
    mid=len(list1)//2
    list2=list1[:mid:]
    list3=list1[mid::]
    if len(list2)!=1:
        list2,count=merge_sort(list2,count)
    if len(list3)!=1:
        list3,count=merge_sort(list3,count)
    return merge(list2,list3,count)

with open("input3.txt","r") as file:
    file.readline()
    arr=list(map(int,file.readline().split()))
    a=merge_sort(arr)
    with open("output3.txt","w") as file1:
        file1.write(str(a[1]))
