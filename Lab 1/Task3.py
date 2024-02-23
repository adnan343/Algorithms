def sorter(arr,arr1):
    size=len(arr)

    for i in range(size):
        min_idx = i

        for j in range(i + 1, size):

            if arr[j] > arr[min_idx]:
                min_idx = j
            elif arr[j] == arr[min_idx]:
                if arr1[j] < arr1[min_idx]:
                    min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        arr1[i], arr1[min_idx] = arr1[min_idx], arr1[i]
    return (arr,arr1)

with open("input3.txt", "r") as file:
  next(file)
  arr = list(map(int,file.readline().split()))
  arr1 = list(map(int,file.readline().split()))
  #print(arr1)
  sorted_arr1, sorted_arr = sorter(arr1,arr)
  with open("output3.txt", "w") as file2:
      for i in range(len(sorted_arr1)):
          a=f"ID: {sorted_arr[i]} Mark: {sorted_arr1[i]}\n"
          #print(a)
          file2.write(a)
