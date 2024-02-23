with open("input1a.txt", "r") as file:
  next(file)
  with open("output1a.txt", "w") as file2:
    for line in file:
      line=line.strip()
      if int(line)%2==0:
          a=line+" is an Even number.\n"
      else:
          a=line+" is an Odd number.\n"
      file2.write(a)