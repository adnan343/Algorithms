def sorter(arr,arr1,arr2):
    size=len(arr)

    for j in range(size):

        for i in range(size-j-1):

            if arr[i] > arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                arr1[i],arr1[i+1]=arr1[i+1],arr1[i]
                arr2[i],arr2[i+1]=arr2[i+1],arr2[i]

            elif arr[i] == arr[i+1]:
                if arr1[i] < arr1[i+1]:
                    arr1[i],arr1[i+1]=arr1[i+1],arr1[i]
                    arr2[i],arr2[i+1]=arr2[i+1],arr2[i]
                    arr[i],arr[i]=arr[i+1],arr[i]

    return (arr,arr1,arr2)


with open("input4.txt", "r") as file:
  n=int(file.readline())
  train_name=[]
  train_destination=[]
  departure_time=[]
  for i in range(n):
      arr = file.readline().split(' ')
      #print(arr)
      train_name.append(arr[0])
      train_destination.append(arr[4])
      departure_time.append(arr[6].strip())


  sorted_name, sorted_departure, sorted_destination = sorter(train_name,departure_time,train_destination)
  with open("output4.txt", "w") as file2:
      for i in range(len(sorted_name)):
          a=f"{sorted_name[i]} will departure for {sorted_destination[i]} at {sorted_departure[i]}\n"
          #print(a)
          file2.write(a)
  # print(train_name)
  # print(train_destination)
  # print(departure_time)

