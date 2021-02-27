import numpy as np
import random
import time

#size = input('Dimensions(x, y): ')
size = '10,10'
#start = input('Start point(x,y): ')
start = '0,0'
#end = input('End point(x,y): ')
end = '9,9'




size = size.split(',')
size = [int(size[n]) for n in range(0,len(size))]

start = start.split(',')
start = [int(start[n]) for n in range(0,len(start))]
        
end = end.split(',')
end = [int(end[n]) for n in range(0,len(end))]

size = [size[1],size[0]]

maze = np.zeros((size[0],size[1]))

#--------------------------------------------
maze[start[1]][start[0]] = 1
maze[end[1]][end[0]] = 1
#--------------------------------------------

print(maze)
x_ = 1
obstacleslist = []

while x_==1:
    obstacles = input('Obstacles(x,y): ')
    if obstacles == '-':
        x_=2
    else:
        obstacleslist.append(obstacles)


        
for i in range(0,len(obstacleslist)):
    obstacleslist[i] = obstacleslist[i].split(',')
    for l in range(0,len(obstacleslist[i])):
        obstacleslist[i][l] = int(obstacleslist[i][l])
        
        x = obstacleslist[i][1]
        y = obstacleslist[i][0]
        #--------------------------------------------
        maze[int(x)][int(y)] = 2
        #--------------------------------------------

finished = False

print(maze)


#-------------------------------------

#heuristics
hs = [] # approx distances from end

nodes = []
nodes.append([start[1],start[0]]) #begin at the start point


#i want a possibilities in every direction one node away from the node. i.e:
#x x x
#x N x
#x x x
g = True

while g == True:
    possibilities = [] #all possibilities for a specific node
    hs = []
    for i in range(0, len(nodes)):
        x = nodes[i][0]
        y = nodes[i][1]

        if x-1 >= start[1] and y+1 >= start[1] and x-1 <= end[1] and y+1 <= end[1]:
            possibilities.append([x-1,y+1])
        if x >= start[1] and y+1 >= start[1] and x <= end[1] and y+1 <= end[1]:
            possibilities.append([x,y+1])
        if x+1 >= start[1] and y+1 >= start[1] and x+1 <= end[1] and y+1 <= end[1]:
            possibilities.append([x+1,y+1])
        if x-1 >= start[1] and y >= start[1] and x-1 <= end[1] and y <= end[1]:
            possibilities.append([x-1,y])
        if x+1 >= start[1] and y >= start[1] and x+1 <= end[1] and y <= end[1]:
            possibilities.append([x+1,y])
        if x-1 >= start[1] and y-1 >= start[1] and x-1 <= end[1] and y-1 <= end[1]:
            possibilities.append([x-1,y-1])
        if x >= start[1] and y-1 >= start[1] and x <= end[1] and y-1 <= end[1]:
            possibilities.append([x,y-1])
        if x+1 >= start[1] and y-1 >= start[1] and x+1 <= end[1] and y-1 <= end[1]:
            possibilities.append([x+1,y-1])


    for i in possibilities:
        if i not in obstacleslist:
            if i not in nodes:

                xs = end[0]-i[0]
                ys = end[1]-i[1]

                hs.append(np.sqrt(xs+ys))
                

        
    for i in possibilities:
        if i not in obstacleslist:
            if i not in nodes:
                xs = end[0]-i[0]
                ys = end[1]-i[1]
                if np.sqrt(xs+ys) == min(hs):
                    nodes.append(i)
                    maze[i[1]][[i[0]]] = '9'

                
        if str(i) == str(end):
            g = False
            maze[i[1]][[i[0]]] = '1'

    print(maze)
    print(nodes)



        
        
                
    

                    
        

    





