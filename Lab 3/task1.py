def merge(list1, list2):
    list3=[]
    i,j=0,0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i+=1
        else:
            list3.append(list2[j])
            j+=1

    if i < len(list1):
        list3.extend(list1[i:])
    elif j < len(list2):
        list3.extend(list2[j:])
    return list3


def merge_sort(list1):
    if len(list1)<=1:
        return list1
    mid=len(list1)//2
    list2=list1[:mid:]
    list3=list1[mid::]
    if len(list2)!=1:
        list2=merge_sort(list2)
    if len(list3)!=1:
        list3=merge_sort(list3)
    return merge(list2,list3)



