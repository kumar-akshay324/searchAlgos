#
# Sample code showing implementation and Visualization of Breadth-First Search and Depth-First Search in a tree with uniform branching factor

import pygame
import math
import time
import random
import numpy as np
from scipy.interpolate import interp1d


def initialize_pygame(config_space_x, config_space_y):				#Setup the pygame environment and ensure returning all created
    pygame.init()
    window_size = [int(config_space_x), int(config_space_y)]
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Breadth-First Search Algorithm -  Akshay Kumar')
    white = 255, 255, 255
    red = 255,0,0
    black = 20, 20, 40
    pink = 255, 0, 255
    screen.fill(white)
    return screen, white, red, black, pink


def visualize_distribution(config_space_x, config_space_y):

    screen, white, red, black, pink  = initialize_pygame(config_space_x, config_space_y)

    # Creating the x axis
    xAxisPointList= [(i,config_space_y/2) for i in range(1,config_space_x, 1)]

    # Creating a cubic spline interpolated random distribution
    xAxisDist = np.linspace(0, config_space_x, num=50, endpoint=True)
    yAxisDist = 99*np.sin(311*xAxisDist)-np.cos(112*xAxisDist)-17*np.tan(12*xAxisDist) #+ 11*np.cot(11*xAxisDist)

    f = interp1d(xAxisDist, yAxisDist, kind = 'cubic')

    xAxisDist2 = np.linspace(0, config_space_x, num=config_space_x+1, endpoint=True)
    # print (f(xAxisDist2))

    DistributionPoints = f(xAxisDist2)
    DistributionPointList = [DistributionPoints[i] + config_space_y/2 for i in range(0, len(DistributionPoints))]

    # Visualizing the distribution and the x-axis
    for index in range(0, len(xAxisPointList)-1):
        pygame.draw.line(screen, black, xAxisPointList[index],xAxisPointList[index+1] , 2)

    for index in range(0, len(DistributionPointList) - 1):
        pygame.draw.line(screen, red, (index, DistributionPointList[index]),(index + 1, DistributionPointList[index+1]) , 2)

    pygame.display.update()
    # time.sleep(1)

    return screen, white, red, black, pink, DistributionPointList, xAxisPointList

def hillClimbing(DistributionPointList, xAxisPointList, screen, white, red, black, pink, resol=1):


    maximaList_x = []
    maximaList_y = []
    maximaList = []

    for i in range(1,100):

        startPointX = random.choice(xAxisPointList)
        # print (startPointX)
        startPoint= startPointX[0]
        loop = True

        while loop==True:

            currentNum =  [startPoint, int(DistributionPointList[startPoint])]
            neighborOne = [startPoint + 1, int(DistributionPointList[startPoint + 1])]
            neighborTwo = [startPoint - 1, int(DistributionPointList[startPoint - 1])]

            # print (currentNum, neighborOne, neighborTwo)

            pygame.draw.circle(screen, red, neighborOne, 5 )
            pygame.draw.circle(screen, red, neighborTwo, 5 )
            pygame.draw.circle(screen, black, currentNum, 5)
            pygame.display.update()
            # time.sleep(0.2)

            if neighborOne[1]<currentNum[1]:
                startPoint = neighborOne[0]

            elif neighborTwo[1]<currentNum[1]:
                startPoint = neighborTwo[0]
            else:
                print ("Locked at local maxima")
                maximaList.append(currentNum)             # [startPoint, currentNum[1]])
                maximaList_x.append(currentNum[0])
                maximaList_y.append(currentNum[1])
                break

    # print (maximaList)
    maxValue_y = min(maximaList_y)

    maxValue_x = maximaList_x[maximaList_y.index(maxValue_y)]

    print (maximaList)
    # print (maxValue_y)
    print (maxValue_x, maxValue_y)

    pygame.draw.circle(screen, black, (maxValue_x, maxValue_y), 25)
    pygame.display.update()

    time.sleep(5)

screen, white, red, black, pink, DistributionPointList, xAxisPointList = visualize_distribution(1600, 1000)
hillClimbing(DistributionPointList, xAxisPointList, screen, white, red, black, pink)