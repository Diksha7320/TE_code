'''
Implement Greedy search algorithm for any of the
following application:
I. Selection Sort
II. Minimum Spanning Tree
III. Single-Source Shortest Path Problem
IV. Job Scheduling Problem
V. Prim's Minimal Spanning Tree Algorithm
VI. Kruskal's Minimal Spanning Tree Algorithm
VII. Dijkstra's Minimal Spanning Tree Algorithm
'''
def selection_sort(array,l):
    for i in range(l):
        min=i
        for j in range(i,l):
            if array[min]>array[j]:
                min=j
        array[i],array[min]=array[min],array[i]
    return array

def prims():
    INF = 9999999
    numVertices = 5
    # create a 2d array of size 5x5
    # for adjacency matrix to represent graph
    mat = [[0 for _ in range(numVertices)] for _ in range(numVertices)]

    print("Enter Number of Edges:")
    numEdges = int(input())
    for i in range(numEdges):
        print("Enter Details of Edge", (i + 1), "as start end weight:")
        start = int(input())
        end = int(input())
        weight = int(input())
        mat[start][end] = weight
        mat[end][start] = weight

    selected = [0 for _ in range(numVertices)]

    no_edge = 0

    selected[0] = True
    # print for edge and weight
    print("Edge : Weight\n")
    while (no_edge < numVertices - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(numVertices):
            if selected[i]:
                for j in range(numVertices):
                    if ((not selected[j]) and mat[i][j]):
                        if minimum > mat[i][j]:
                            minimum = mat[i][j]
                            x = i
                            y = j
        print(str(x) + "-" + str(y) + ":" + str(mat[x][y]))
        selected[y] = True
        no_edge += 1

        
    
print("Enter Choice:")
print("1.selectionsort")
print("2.prims")
choice=int(input("Choice:"))
if(choice==1):
    arr=[]
    l=int(input("Enter lenth of array : "))
    for i in range(l):
        arr.append(int(input("Enter number : ")))

    arr=selection_sort(arr,l)

    print(arr)
elif(choice==2):
    prims()
else:
    print("invalid input")
    
