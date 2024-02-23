def bubbleSort(arr):
    for i in range(len(arr)-1):
      flag=0
      for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                flag+=1
                arr[j], arr[j+1] = arr[j+1], arr[j]
      if flag==0:
        break
    return arr

with open("input2.txt", "r") as file:
  next(file)

  arr=file.readline().split()
  for i in range(0,len(arr)):
    arr[i]=int(arr[i])

  with open("output2.txt","w") as file2:
    arr1=bubbleSort(arr)
    for i in arr1:
        file2.write(str(i)+" ")
