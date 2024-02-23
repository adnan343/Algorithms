def sum_finder(list1,integer):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if int(list1[i])+int(list1[j])==integer and i!=j:
                return f"{i+1} {j+1}"
    return "IMPOSSIBLE"

with open("task1in.txt", "r") as file:
    sum = file.readline().strip().split()
    sum=int(sum[-1])
    arr = file.readline().strip().split()
    with open("task1out1n^2.txt", "w") as file2:
        file2.write(sum_finder(arr, sum))