#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 14:24:04 2025

CHEM 272 Project 1

@author: joe21
"""

import numpy as np
import matplotlib.pyplot as plt
#inputs:
    
N: int = 400
dt: float = 10**(-3)
Total_iterations: int = 10000
display_freq: int = 100
pos_min_X: float = -100 
pos_max_X = 100
pos_min_Y: float = -100
pos_max_Y: float= 100
vel_X_init_mu: float = 0
vel_X_init_std: float = 0.5 
vel_Y_init_mu: float = 0
vel_Y_init_std: float = 1 
mass_min: float = 1
mass_max: float = 10
c: float = 0.001
max_BirdDisplaySize: float = 75 
Bird_ColorMap: str = 'viridis' 
a: float = 163840 
b: float = 2560
Temp: float = 2

    
#initial setup:
#set uniformly distrubuted random positions:
pos_X = np.random.uniform(pos_min_X, pos_max_X, (N,1))
pos_Y = np.random.uniform(pos_min_Y, pos_max_Y, (N,1))


#set uniformly distributed random Bird weights:
particle_mass = np.random.uniform(mass_min,mass_max,(N,1))

#normalize the bird weights from 0 to 1 for graphing color and marker size:
normalized_birdMass = particle_mass/mass_max
bird_sizeDisplay = max_BirdDisplaySize *normalized_birdMass

#Plot the initial Bird Positions:
plt.scatter(pos_X,pos_Y, s= bird_sizeDisplay, c=normalized_birdMass, cmap=Bird_ColorMap)
plt.xlabel('X-Position (length units)')
plt.ylabel('Y-Position (length units)')
plt.title('Initial Particle Location\n Interation# ' +str(0) )
plt.show()

sumCols = np.ones((N,1))
#---------------------
#Loop:
for loop in range(0,Total_iterations):
    #set normally distrubited random steps:
    step_X = np.random.normal(vel_X_init_mu, vel_X_init_std, (N,1))
    step_Y = np.random.normal(vel_Y_init_mu, vel_Y_init_std, (N,1))
    
    posX_2check = pos_X + step_X 
    posY_2check = pos_Y + step_Y 
    
    #Calculate distance^2 between each particle:
    dX2_last = np.dot((pos_X - pos_X.transpose())**2,sumCols) 
    dY2_last = np.dot((pos_Y - pos_Y.transpose())**2,sumCols) 
    
    #dX2_last = np.dot((pos_X - pos_X.transpose())**2,axis=1) 
    #dY2_last = np.dot((pos_Y - pos_Y.transpose())**2,axis=1)
    r2_last = dX2_last + dY2_last
    
    
    
    dX2_check = np.dot((posX_2check - posX_2check.transpose())**2,sumCols) 
    dY2_check = np.dot((posY_2check - posY_2check.transpose())**2,sumCols) 
    #dX2_check = np.sum((posX_2check - posX_2check.transpose())**2,,axis=1) 
    #dY2_check = np.sum((posY_2check - posY_2check.transpose())**2,,axis=1) 
    
    
    r2_check = dX2_check + dY2_check
    
    
    U_last = a*r2_last**(-6) - b*r2_last**(-3)
    U_check = a*r2_check**(-6) - b*r2_check**(-3)
    
    dU = U_last - U_check
    rho = np.random.uniform(0,1,(N,1))
    p_move = np.exp(-dU/Temp)
    
    stepCondition = (dU<0) | ((dU>0)&(rho<p_move))
    pos_X += step_X*stepCondition
    pos_Y += step_Y*stepCondition
    
    if (loop+1) % display_freq == 0:
        #Plot the initial Bird Positions:
        plt.scatter(pos_X,pos_Y, s= bird_sizeDisplay, c=normalized_birdMass, cmap=Bird_ColorMap)
        plt.xlabel('X-Position (length units)')
        plt.ylabel('Y-Position (length units)')
        plt.title('Particle Location\n Interation# ' +str(loop+1) )
        plt.show() 
 
    
   
    
    
    