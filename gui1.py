# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter import ttk
from BFS_DFS import *
from Astar import *
root=Tk()
style=ttk.Style()
var = StringVar()
rows, cols = (3, 3)
entries = [[0 for i in range(cols)] for j in range(rows)]
for i in range(3):
    for j in range(3):
        entries[i][j]=ttk.Entry(root,justify='center',background='red',width=10,font=("Courier 20 bold"))
        entries[i][j].grid(row=i,column=j,sticky='snew',ipady=10)

stop=ttk.Button(root,text="Stop")
stop.grid(row=4,column=0,sticky='snew',ipady=10)
nextButt=ttk.Button(root,text='Next')
BFS=ttk.Button(root,text='BFS')
DFS=ttk.Button(root,text='DFS')
AStarEq=ttk.Button(root,text='A star Euclidean')
AStar=ttk.Button(root,text='A star Manhattans')
BFS.grid(row=3,column=2,sticky='snew',ipady=10)
DFS.grid(row=3,column=1,sticky='snew',ipady=10)
AStar.grid(row=4,column=1,sticky='snew',ipady=10)
AStarEq.grid(row=4,column=2,sticky='snew',ipady=10)

#nextButt.grid(row=3,column=1,sticky='snew',ipady=10)

#var.trace(mode="w", callback=callback)
'''def change_color():
    for i in range(len(entries)):
        for j in range(len(entries[i])):
            if(int(entries[i][j].get())==0):
                print("hey bby")
                entries[i][j].configure(background= 'white')
            else:
                print("hey man")
                entries[i][j].configure(background= 'red')'''
# Method to change array after each state
def change_array(state):
    counter = 0
    #change_color()
    for i in range(len(entries)):
        for j in range(len(entries[i])):
            if(state[counter]==0):
                entries[i][j].delete(0, END)
                counter+=1
            else:
                entries[i][j].delete(0, END)
                entries[i][j].insert(END, state[counter])
                counter += 1
                #change_color()

# the main method that solves the puzzle depending on the clicked button
def solve(method):
    '''take entries of the input array'''
    array=[]
    for i in range (len(entries)):
        for j in range(len(entries[i])):
            array.append(int(entries[i][j].get()))
    print(array)

    if not(check_solvablability(array)):
        steps = ttk.Label(root, text="Not solvable", justify='center', width=10,
                          font=("Courier 20 bold"))
        steps.grid(row=3, column=0, sticky='snew', ipady=10)
    else:


        #choose the algorithm that will solve the problem

        n=None
        if(method=="bfs"):
             n = Node(array, None, 0)
             n=bfs(n)
        elif(method=="dfs"):
             n = Node(array, None, 0)
             n=dfs(n)
        elif(method=="Star_Euclidean"):
            array = coonvert_array(array, method)
            n = Node_Astar(array, None)
            n=Astar_solver(n,"Euclidean")
        elif(method=="Star_Manhattan"):
            array = coonvert_array(array, method)
            n = Node_Astar(array, None)
            n = Astar_solver(n, "Manhattan")



        stack=[]
        while n != None:

            stack.append(n.step)
            n = n.parent
        #this function make code wait after each step
        def waithere():
            var = IntVar()
            root.after(1000, var.set, 1)
            root.wait_variable(var)
        step_counter=0
        while (stack):
            steps = ttk.Label(root, text="Steps = " + str(step_counter), justify='center', width=10, font=("Courier 20 bold"))
            steps.grid(row=3, column=0, sticky='snew', ipady=10)
            waithere()
            step=stack.pop()
            if(method=="Star_Euclidean"or method=="Star_Manhattan"):
                list=[]
                counter=0
                for i in range(3):
                    for j in range(3):
                        list.append(step[i][j])
                        counter+=1
                step=list
            change_array(step)
            step_counter = step_counter + 1

def coonvert_array(n,method):
    if (method == "Star_Euclidean" or method == "Star_Manhattan"):
        newN= [[0 for i in range(3)] for j in range(3)]
        counter=0
        for i in range(3):
            for j in range(3):
                newN[i][j]=n[counter]
                counter+=1
    return newN


BFS.config(command=lambda :solve("bfs"))
DFS.config(command=lambda :solve("dfs"))
AStarEq.config(command=lambda :solve("Star_Euclidean"))
AStar.config(command=lambda :solve("Star_Manhattan"))
root.mainloop()


