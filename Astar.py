import time
import math
from queue import PriorityQueue
from collections import deque
import copy
from itertools import count


class Node_Astar:
    def __init__(self, step, parent=None):
        self.step = step
        self.parent = parent

        if (self.parent != None):
            self.g = parent.g + 1
        else:
            self.g = 0



def hManhattan(x):
    statex = x.step
    distance = 0
    for i in range(3):
        for j in range(3):
            if statex[i][j] != 0:
                # x , y = the position of state[i][j] in the final state
                x, y = divmod(statex[i][j], 3)
                distance += abs(x - i)  + abs(y - j)
    return distance

def hEuclidean(x):
    statex = x.step
    distance = 0
    for i in range(3):
        for j in range(3):
            if statex[i][j] != 0:
                # x , y = the position of state[i][j] in the final state
                x, y = divmod(statex[i][j] , 3)
                distance += int(math.sqrt(abs(x - i) ** 2 + abs(y - j) ** 2))
    return distance

#method = "Manhattan"

def f(x,method):

    if method == "Manhattan" :
        return hManhattan(x) + x.g
    else:
        return hEuclidean(x) + x.g

def printPath(x):

    stack = deque()

    while(x != None) :
        stack.append(x)
        x = x.parent

    numberOfsteps = 0

    while stack :
        x = stack.pop()

        print("step number :" + str(numberOfsteps))
        numberOfsteps += 1
        #print state of each node
        for i in range(0, 3):
            print(x.step[i])
        print()

    print("Toltal number Of steps :" + str(numberOfsteps-1) + " steps")


##########these funtion is to get childerns of node

def emptyLocation(arr):
    for i in range(3):
        for j in range(3) :
            if(arr[i][j]==0):
                return i,j

def MoveUp(empty_space,arr):
    newArray = copy.deepcopy(arr)
    i , j = empty_space
    if (i != 0) :
        x = newArray[i-1][j]
        newArray[i-1][j] = newArray[i][j]
        newArray[i][j] = x

    return newArray

def MoveDown(empty_space,arr):
    newArray = copy.deepcopy(arr)
    i, j = empty_space
    if (i != 2):
        x = newArray[i+1][j]
        newArray[i+1][j] = newArray[i][j]
        newArray[i][j] = x

    return newArray

def MoveLeft(empty_space,arr):
    newArray = copy.deepcopy(arr)
    i, j = empty_space
    if (j != 0):
        x = newArray[i][j-1]
        newArray[i][j-1] = newArray[i][j]
        newArray[i][j] = x

    return newArray

def MoveRight(empty_space,arr):
    newArray = copy.deepcopy(arr)
    i, j = empty_space
    if (j != 2):
        x = newArray[i][j+1]
        newArray[i][j+1] = newArray[i][j]
        newArray[i][j] = x

    return newArray


#Generate all possible children for the current state
def generateChildren(frontierSet,frontierQueue,explored,node,method) :
    state = node.step
    empty_space = emptyLocation(state)

    list = []
    new_state = MoveUp(empty_space,state)
    if (new_state != state) :
        list.append(new_state)
    new_state = MoveDown(empty_space, state)
    if (new_state != state):
        list.append(new_state)
    new_state = MoveLeft(empty_space, state)
    if (new_state != state):
        list.append(new_state)
    new_state = MoveRight(empty_space, state)
    if (new_state != state):
        list.append(new_state)

    for array in list :
        #for each new child
        #if this child is exist in explore set then dont add it
        if str(array) in explored :
            continue


        #if this child is not repeated just add it to frontierqueue
        if str(array) not in frontierSet :
            newNode = Node_Astar(array, node)
            frontierSet.add(str(array))
            frontierQueue.put((f(newNode,method),next(unique),newNode))

        else :
            #the child is repeated
            #search in the frontierQueue for this state
            s = deque()

            while not frontierQueue.empty() :
                x = frontierQueue.get()
                s.append(x)
                score = x[0]
                currentNode = x[2]

                if (currentNode.step == array) :
                    if (score > f(Node_Astar(array), method)) :
                        newNode = Node_Astar(array, node)
                        frontierQueue.put((f(newNode,method),next(unique),newNode))
                        s.pop()
                        break

            while s :
                frontierQueue.put(s.pop())

finalState = [[0,1,2],[3,4,5],[6,7,8]]

def Astar_solver(intial_state, method):
    #intial state is a node
    frontier = PriorityQueue()
    frontier.put((f(intial_state,method),next(unique),intial_state))

    frontierSet = set();
    frontierSet.add(str(intial_state.step))

    explored = set()

    maxDepth = 0
    start=time.time()
    while not frontier.empty() :
        # x is the node with the samllest f in the queue
        x = frontier.get()[2]
        stateX = x.step



        if  stateX == finalState :
            print("got it")

            if (x.g > maxDepth):
                maxDepth = x.g

            printPath(x)
            end=time.time()
            print("Max Depth : ", str(maxDepth))
            print("Total number of explores nodes : ", len(explored), " node(s)")
            print("Total amount of time : ", str(end - start), " second(s)")
            return x

        else :
            if str(stateX) not in explored :
                generateChildren(frontierSet,frontier,explored,x,method)
                explored.add(str(stateX))

                #get the maxDepth which is the greater g we vidited
                if(x.g > maxDepth) :
                    maxDepth = x.g

def check_solvablability_Astar(initial_state):
    arr = []
    for i in range(0,3):
        for j in range(0, 3):
            arr.append(initial_state[i][j])

    inv = 0
    for i in range(8):  # Check Solvability
        for j in range(i, 9):
            if arr[i] > arr[j] and arr[j] != 0:
                inv = inv + 1
    if inv % 2 != 0:  # Exit if not solvable
        print("No solution exists for this initial state")
        return False
    return True


unique = count()
'''intial_state = []

print("enter the initaila state of the puzzle as 3*3 matrix each number in single line")
print("Note : make sure that each number in single line")

for i in range(3):          # A for loop for row entries
    a =[]
    for j in range(3):      # A for loop for column entries
         a.append(int(input()))
    intial_state.append(a)


print(intial_state)



if check_solvablability_Astar(intial_state) :
    print("Choose The Type of A* : 1 - Manhattan\n\t\t\t\t\t 2 - Euclidean")
    m = input()
    if m == '1' :
        method = "Manhattan"
    else :
        method = "Euclidean"



    node = Node_Astar(intial_state)

    #this unique counter is used to make the PriorityQueue work properly as
    # if PriorityQueue has to nodes with the same f value
    # then it cant work property as it cant compare two nodes
    

    tic = time.time()
    explored , maxDepth,node= Astar(node,"Manhattan")
    toc = time.time()

#print("Max Depth : ",str(maxDepth))
#print("Total number of explores nodes : ",explored," node(s)")
print("Total amount of time : ",str(toc - tic)," second(s)")'''


