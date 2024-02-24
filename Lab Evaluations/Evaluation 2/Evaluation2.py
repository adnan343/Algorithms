def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return arr


with open('input.txt', 'r') as file:
    file.readline()
    pivot = file.readline().strip().split()
    arr = file.readline().strip().split()

for i in pivot:
    arr.append(i)
    arr = partition(arr, 0, len(arr)-1)
arr = str(arr).replace('[', '').replace(']', '').replace("'", '').replace(",",'')
with open('output.txt', 'w') as file1:
    file1.write(arr)
