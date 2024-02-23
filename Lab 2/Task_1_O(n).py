def checker(arr,sum):
  p1=0
  p2=len(arr)-1
  while p1<p2:
    if int(arr[p1])+int(arr[p2])==int(sum):
      p1n=p1+1
      p2n=p2+1
      return f"{p1n} {p2n}"
    elif int(arr[p1])+int(arr[p2])>int(sum):
      p2-=1
    else:
      p1+=1
  return "IMPOSSIBLE"

with open("task1in.txt","r") as file:
  sum=file.readline().strip().split()
  sum=sum[-1]
  arr=file.readline().strip().split()
  with open("task1out1n.txt","w") as file2:
    file2.write(checker(arr,sum))
