def calculate(a,b,c):
  if b=='+':
    return a+c
  elif b=='-':
    return a-c
  elif b=='/':
    return a/c
  elif b=='*':
    return a*c

with open("input1b.txt", "r") as file:
  next(file)
  with open("output1b.txt", "w") as file2:
    for line in file:
      line=line.strip()
      arr=line.split()
      a=f"The result of {arr[1]} {arr[2]} {arr[3]} is {calculate(int(arr[1]),arr[2],int(arr[3]))}\n"
      file2.write(a)