from queue import Queue
import numpy
from anytree import Node, RenderTree
import time

def is_valid(i,j,n,m):
    return i >= 0 and i < n and j >= 0 and j < m

binaryImage=open("ID.txt")
maze=[]
for line in binaryImage:
    row=[int(d) for d in str(int(line))]
    maze.append(row)    
visited= numpy.zeros((len(maze),len(maze[0])))

def breadthFirstSearch(start, goal):
    start_time=time.time()
    queue = Queue()
    i, j = start.split(',')
    visited[int(i),int(j)]=1
    root= Node(i+","+j)
    currentNode=root
    goalNode=None
    n=len(maze)
    m=len(maze[0])
    queue.put(root)

    while not queue.empty():
        currentNode = queue.get()
        if currentNode.name == str(goal):
            goalNode=currentNode
            break
        i, j = currentNode.name.split(',')
        i=int(i)
        j=int(j)
        for x, y in [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]: # directions
            if (is_valid(i+x, j+y,n,m) and not visited[i+x,j+y] and maze[i+x][j+y]):
                node=Node(str(i+x) + "," + str(j+y), parent=currentNode)
                queue.put(node)
                visited[i+x,j+y]=1
                if node.name == str(goal):
                    goalNode=node
                    break
            
    for node in currentNode.iter_path_reverse():
        i, j = node.name.split(',')
        i=int(i)
        j=int(j) 
        maze[i][j] =2
       
    end_time = time.time()
    print("Time Of Search:"+""+ str(end_time-start_time))

    from matplotlib import pyplot as plt
    plt
    plt.imshow(maze, interpolation='nearest')
    plt.show()
    ##if you want to print the tree uncomment the two lines below
    ##for pre, fill, node in RenderTree(root):
    ##    print("%s%s" % (pre, node.name))
    
			#Main
start= str(input("Enter your start position : "))
goal = str(input("Enter your goal position : "))
breadthFirstSearch(start,goal)
