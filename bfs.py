#
# Sample code showing implementation and Visualization of Breadth-First Search and Depth-First Search in a tree with uniform branching factor

import pygame
import math
import time

arr = []

def initialize_pygame(config_space_x, config_space_y):				#Setup the pygame environment and ensure returning all created
    pygame.init()
    window_size = [int(config_space_x), int(config_space_y)]
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Breadth-First Search Algorithm -  Akshay Kumar')
    white = 255, 240, 200
    red = 255,0,0
    black = 20, 20, 40
    pink = 255, 0, 255
    screen.fill(white)
    return screen, white, red, black, pink

def create_tree(depth_level, branch_fac, config_space_x, config_space_y):

    ind_fc = 0
    arr = [[0]*int(math.pow(branch_fac, i)) for i in range(0,depth_level+1)]
    screen, white, red, black, pink  = initialize_pygame(config_space_x, config_space_y)
    print ("Depth of the tree is %d" %(len(arr)))
    ind_depth = [len(ar) for ar in arr ]
    print (ind_depth)

    for k in range(0, len(arr)):
        for index in range(0, len(arr[k])):
                pygame.draw.circle(screen, pink, ((config_space_x*(index+1)/(len(arr[k])+1)), 50 + k*50), 10)
                pygame.display.update()
                arr[k][index] = tuple(((config_space_x*(index+1)/(len(arr[k])+1)), 50 + k*50))
    for p in range(0, len(arr)-1):
        for q in range(0, len(arr[p])):
            for index in range(0, branch_fac):
                pygame.draw.line(screen, red, arr[p][q],arr[p+1][ind_fc])
                pygame.display.update()
                ind_fc +=1
        ind_fc = 0
    time.sleep(1)
    print (arr)
    return arr, screen, white, red, black, pink

def bfs(arr, screen, black, goal=0):
    success = False
    if goal==0:
        goal = arr[-1][-1]
    for p in range(0, len(arr)):
        for index in range(0, len(arr[p])):
            if (p,index)==goal:
                pygame.draw.circle(screen, black,arr[p][index], 20)
                pygame.display.update()
                success = True
                break
            else:
                pygame.draw.circle(screen, black, arr[p][index], 7)
                pygame.display.update()
            time.sleep(0.2)
        if success ==True:
            print ("Hurray, the search was successful")
            break
    time.sleep(1)



arr, screen, white, red, black, pink = create_tree(5,2, 1500, 500)
bfs(arr,screen, black,(4,14))
