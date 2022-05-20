# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy
import time


class Node:
    def __init__(self, step, parent=None,g=None):
        self.step = step
        self.parent = parent
        self.g=g


# get the empty tile of the array
def emptyLocation(arr):
    for i in range(9):
        if (arr[i] == 0):
            return i


# get the move down state if possible
def MoveDown(e, arr):
    u = copy.deepcopy(arr)
    if (e < 6):
        u[e] = u[e + 3]
        u[e + 3] = 0
    return u


# get the move Up state if possible
def MoveUp(e, arr):
    u = copy.deepcopy(arr)
    if (e > 2):
        u[e] = u[e - 3]
        u[e - 3] = 0
    return u


# get the move left state if possible

def MoveLeft(e, arr):
    u = copy.deepcopy(arr)
    if ((e != 0) & (e != 3) & (e != 6)):
        u[e] = u[e - 1]
        u[e - 1] = 0
    return u


# get the move right state if possible

def MoveRight(e, arr):
    u = copy.deepcopy(arr)
    if ((e != 2) & (e != 5) & (e != 8)):
        u[e] = u[e + 1]
        u[e + 1] = 0
    return u


def takeInput():
    arr = [int(i) for i in input().split()]
    return arr


# check if the intial state is solvable or not
def check_solvablability(arr):
    inv = 0
    for i in range(8):  # Check Solvability
        for j in range(i, 9):
            if arr[i] > arr[j] and arr[j] != 0:
                inv = inv + 1
    if inv % 2 != 0:  # Exit if not solvable
        print("No solution exists for this initial state")
        return False
    return True


# Generate all possible children for the current state
def generateChildren(stack, node,explored):
    step = node.step
    b = emptyLocation(step)
    new_step = MoveUp(b, step)
    if (new_step != step ):
        if not str(new_step) in explored:
            stack.append(Node(new_step, node,node.g+1))
    new_step = MoveDown(b, step)
    if (new_step != step):
        if not str(new_step) in explored:
            stack.append(Node(new_step, node,node.g+1))
    new_step = MoveLeft(b, step)
    if (new_step != step):
        if not str(new_step) in explored:
            stack.append(Node(new_step, node,node.g+1))
    new_step = MoveRight(b, step)
    if (new_step != step):
         if not str(new_step) in explored:
            stack.append(Node(new_step, node,node.g+1))

def bfs(intial_node):
    search_deapth=0
    explored = set()
    queue = []
    queue.append(intial_node)
    start = time.time()
    while (queue):
        current_node = queue.pop(0)
        if(current_node.g>search_deapth):
            search_deapth=current_node.g
        if (current_node.step == [0, 1, 2, 3, 4, 5, 6, 7, 8]):
            print_steps(current_node, explored)
            end = time.time()
            print("Consumed time = " + str(end - start) + " s")
            print("Search Depth=" + str(search_deapth))
            return current_node

        if not str(current_node.step) in explored:
            generateChildren(queue, current_node,explored)
            explored.add(str(current_node.step))


def dfs(intial_node):
    search_deapth = 0
    explored = set()
    stack = []
    stack.append(intial_node)
    start = time.time()
    while (stack):
        current_node = stack.pop()
        if (current_node.g > search_deapth):
            search_deapth = current_node.g
        if (current_node.step == [0, 1, 2, 3, 4, 5, 6, 7, 8]):
            end = time.time()
            print_steps(current_node, explored)
            print("Consumed time = " + str(end - start) + " s")
            print("Search Depth=" + str(search_deapth))
            return current_node

        if not str(current_node.step) in explored:
            generateChildren(stack, current_node,explored)
            explored.add(str(current_node.step))


def print_array(array):
    for i in range(0, 9, 3):
        for j in range(3):
            print(array[i + j], end=" ")
        print()


def print_steps(Node, explored):
    stack = []
    while (Node.parent != None):
        stack.append(Node.step)
        Node = Node.parent
    step_number = 1
    while (stack):
        print("Step " + str(step_number) + " :")
        print_array(stack.pop())
        step_number += 1
    print()
    print("Explored Nodes: " + str(explored.__sizeof__()))


'''print("enter input like that: 1 5 2 0 6 3 4 7 8")
u = takeInput()
if  (check_solvablability(u)):
    print('Choose (1) for BFS\n      (2) for DFS')
    x=input()
    if(x=='1'):
        print("Solution With BFS :")
        node = Node(u, None,0)
        start = time.time()
        final_node= bfs(node)
        end= time.time()
        x = end-start
    else:
        print("Solution With DFS :")
        node = Node(u, None, 1)
        start = time.time()
        dfs(node)
        end = time.time()
        x = end - start'''





