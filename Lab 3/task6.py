def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSelect(arr, low, high, th):
    if low < high:
        p = partition(arr, low, high)
        if p == th-1:
            return arr[p]
        if p < th:
            a=quickSelect(arr, p+1, high, th)
        else:
            a=quickSelect(arr, 0, p-1, th)
    return a


with open("input6.txt", "r") as file:
    file.readline()
    arr = list(map(int, file.readline().split()))
    n = int(file.readline()[0])
    with open("output6.txt", "w") as file1:
        file1.flush()
        string=''
        for i in range(n):
            th = int(file.readline())
            a = quickSelect(arr, 0, len(arr)-1, th)
            string+=str(a)+"\n"
        file1.write(string)
        file1.close()