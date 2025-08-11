#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 11:53:28 2025

@author: katrinareyes
"""
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
    N = len(x)
    X_i = np.tile(x, (N, 1))
    diff_x_matrix = np.abs(X_i - X_i.T) #vectorized form to find distance between x values faster
    
    len(y) == N
    Y_i = np.tile(y, (N,1)) #vectorized form to find distnace between y values faster
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
        
        dx = np.random.uniform(-1, 1)
        dy = np.random.uniform(-1, 1)

        x_new_test[k] = x[k] + dx
        y_new_test[k] = y[k] + dy
        U_tot_new = Potential(x_new_test,y_new_test,a,b)
        
        diff_Utot = U_tot_new - Utot
        if diff_Utot <= 0:
            x[k] += dx
            y[k] += dy
            Utot = U_tot_new
            
        elif diff_Utot >0:
            p_move = np.exp(-diff_Utot/T)
            rho = np.random.uniform(0,1)
            if rho < p_move:
                x[k] += dx
                y[k]  += dy
                Utot = U_tot_new
      
            
    return x,y, Utot

def plot_ParticleLocations(x,y,i):
    
    plt.figure()
    plt.scatter(x,y, alpha = 0.3)
    plt.title(f'Particle 2D Positions: Iteration {i}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# def plot_Utot_histograms(iterations, N, Utot):
    
#     for i in range(iterations):
#         if i%100 ==0:
#             plt.hist(Utot, N, density = False, histtype = 'step', facecolor = 'g', alpha = 0.75)
#             plt.xlabel('Total Potential')
#             plt.ylabel('Number of Particles')
#             plt.title(F'Total Potential Distribution: Iteration {i}')
#             plt.show()
            #Keep a history of energy per iteration and position snapshots for scatter frames
        
    
    
class Simulate_Particle():
    
    def __init__(self, iterations = 100000, N = 100, a = 1, b = 1, T = 37.0):
        
        self = self
        self.iterations = iterations
        self.N = N
        self.a = a
        self.b = b
        self.T = T
        
        self.x, self.y = Plot_Location(N)
        self.Utot = Potential(self.x, self.y, a,b)
        # self.U_history = []
       
          
        
    def run(self):
        with PdfPages("all_particle_plots.pdf") as pdf:
            for i in range(self.iterations):
                self.x, self.y, self.Utot = Move_Particle(self.x, self.y, self.a, 
                                                          self.b, self.Utot, self.N, self.T)
                # self.U_history.append(self.Utot)
                
                if i % 100 == 0:
                    plot_ParticleLocations(self.x, self.y, i)
                # plot_Utot_histograms(self.U_history, self.N, i)
                
sim = Simulate_Particle(iterations=1000, N=100, a=1, b=1, T=37.0)
sim.run()
    
