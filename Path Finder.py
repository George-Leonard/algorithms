import numpy as np
import random
import time


#user friendly

#size = input('Dimensions(x, y): ')
#start = input('Start point(x,y): ')
#end = input('End point(x,y): ')

size = '10,10'
start = '9,0'
end = '0,9'



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

#user friendly

#while x_==1:
   #obstacles = input('Obstacles(x,y): ')
    #if obstacles == '-':
        #x_=2
    #else:
        #obstacleslist.append(obstacles)


        
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

already = []
avail = []
while finished == False:

    newcells = []
    for i in range(0, len(maze)):
        for x in range(0, len(maze[i])):
            #print([i],[x])
            #print(maze[x][i])
            avail.append([x,i])

    for i in range(0,len(avail)):
        w = avail[i][0]
        z = avail[i][1]
        if w-1==start[0] or z-1==start[1] or w+1==start[0] or z+1==start[1]:
            if z==start[1]:
                newcells.append(avail[i])
            if w==start[0]:
                newcells.append(avail[i])
            else:
                pass

    try:
        start = random.choice(newcells)
        if maze[start[1]][start[0]] != 2:
            maze[start[1]][start[0]] = 1
            print(maze)
        if start[1] == end[1] and end[0]-start[0]==1:
            print('finished')
            break
        if start[0] == end[0] and end[1]-start[1]==1:
            print('finished')
            break
    except:
        break
print(maze)
        
        
        
                
    

                    
        

    





