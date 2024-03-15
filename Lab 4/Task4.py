class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [0] * v
        for i in range(self.v):
            self.adj[i] = []

    def addedge(self, i,j):
        self.adj[i].append(j)

    def isCyclic(self):
        visited = [False] * self.v
        helper = [False] * self.v
        for i in range(self.v):
            if visited[i] == False:
                ans = self.DFS(i,visited,helper)
                if ans == True:
                    return True
        return False


    def DFS(self,i, visited,helper):
        visited[i] = True
        helper[i] = True
        neighbours = self.adj[i]
        for k in range(len(neighbours)):
            curr = neighbours[k]
            if helper[curr] == True:
                return True
            if visited[curr] == False:
                ans = self.DFS(curr,visited,helper)
                if ans == True:
                    return True
        helper[i] = False
        return False


with open("input4.txt","r") as file:
    a = list(map(int, file.readline().split()))
    n = int(a[0])
    m = int(a[1])
    arr = []
    for i in range(m):
        arr.append(list(map(int, file.readline().split())))
    #print(arr)
    g = Graph(n+1)
    for i in range(m):
        g.addedge(arr[i][0],arr[i][1])



    if g.isCyclic() == 1:
        a = "Yes"
    else:
        a = "No"

    with open("output4.txt","w") as file1:
        file1.write(a)