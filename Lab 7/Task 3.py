def fib(n):
    if n <= 1:
        return n
    fib = [0]*(n+1)
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

with open("input3.txt","r") as file:
    n = int(file.readline())
    result = fib(n+1)
    with open("output3.txt","w") as file1:
        file1.write(str(result))
