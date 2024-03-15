def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)
    return arr

with open("input5.txt","r") as file:
    file.readline()
    arr=list(map(int,file.readline().split()))
    a=quickSort(arr,0,len(arr)-1)
    a=str(a).replace(",", "")
    with open("output5.txt","w") as file1:
        file1.write(str(a[1:-1:]))

