def selector(a1,a2,k):

  list1 = []
  i=0
  j=0
  n=0

  while i < len(a1) and j < len(a2):
    if a1[i] < a2[j]:
      list1.append(a1[i])
      i += 1
      n += 1
    else:
      list1.append(a2[j])
      j += 1
      n += 1
    if n == k:
      return list1[k-1]

  if i < len(a1):
    list1 += a1[i:]
  if j < len(a2):
    list1 += a2[j:]
  return list1[k-1]


with open('input.txt', 'r') as file:
    file.readline()
    a1 = list(map(int, file.readline().split()))
    file.readline()
    a2 = list(map(int, file.readline().split()))
    k = int(file.readline().strip())
    val = selector(a1,a2,k)
    with open('output.txt', 'w') as file1:
        file1.write(str(val))