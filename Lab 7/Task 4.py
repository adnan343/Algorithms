def ccp(arr, target):
    result = [target+1]*(target+1)
    result[0]=0
    for i in range(1, len(result)):
        for j in arr:
            if j <= i:
                result[i] = min(result[i], result[i-j]+1)
    return result[-1]

with open ("input4.txt", "r") as file:
    target = list(map(int, file.readline().split()))[-1]
    arr = list(map(int, file.readline().split()))
    result = ccp(arr, target)
    with open("output4.txt", "w") as file1:
        file1.write(str(result))
