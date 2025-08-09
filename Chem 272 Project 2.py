#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 11:53:28 2025

@author: katrinareyes
"""
import numpy as np
import matplotlib.pyplot as plt

def Plot_Location(particle_count):
    x = np.random.uniform(-100, 100, particle_count)
    y = np.random.uniform(-100,100, particle_count)
    return x, y

def Potential(x,y,a,b):
    X_i = np.tile(x, (particle_count, 1))
    diff_x_matrix = np.abs(X_i - X_i.T) #vectorized form to find distance between x values faster
    

    Y_i = np.tile(y, (particle_count,1)) #vectorized form to find distnace between y values faster
    diff_y_matrix = np.abs(Y_i - Y_i.T)
    
    r = np.sqrt(diff_x_matrix**2 + diff_y_matrix**2)
    r = np.clip(r, 0.0001,100)
    potential_ij = (a/(r**12)) - (b/(r**6))
    np.fill_diagonal(potential_ij, 0)
    Utot = np.sum(potential_ij)/2
    
    return Utot
    
 
def Move_Particle(x,y,a,b,Utot, particle_count,T):
    for k in range(particle_count):
        x_new_test =  x.copy()
        y_new_test = y.copy()
        x_new_test[k] = x[k] + 0.01
        y_new_test[k] = y[k] + 0.01
        U_tot_new = Potential(x_new_test,y_new_test,a,b)
        
        diff_Utot = U_tot_new - Utot
        if diff_Utot <= 0:
            x[k] = x[k]+0.01
            y[k] = y[k] + 0.01
            Utot = U_tot_new
            
        elif diff_Utot >0:
            p_move = np.exp(-diff_Utot/T)
            rho = np.random.uniform(0,1)
            if rho < p_move:
                x[k] = x[k]+0.01
                y[k] = y[k] + 0.01
                Utot = U_tot_new
            else: 
                pass
            
            
    return x,y
                
        
    
    #if dUtot<0 always move
    #id fUtot>0, draw a random number between 0 to 1 and see if its less than pmove if so, move
class Simulate_Particle():
    
    def __init__(self):
        
    def run():
        
        