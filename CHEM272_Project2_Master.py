
#import libraries
import numpy as np
import matplotlib.pyplot as plt

def CoordsToPotential(Xin, Yin, a, b, N, Eye, Ones):
    
    X      = np.tile(Xin, (N,1))
    Y      = np.tile(Yin, (N,1))
    
    Dx     = X - X.transpose()
    Dy     = Y - Y.transpose()

    r2 = Dx**2 + Dy**2
    r2 = r2 + (Eye*(10**16))

    
    Phi = ((a / r2**6) - (b / r2**3))
    
    Utot = np.dot(Phi, Ones)

    return Utot

def PotentialToMotion(iterations, N, a, b, T, step_size):

    Eye  = np.eye(N)
    Ones = np.ones((N, ))
    
    #ininitiate random positions in xy plane
    Xinit = np.random.uniform(-100, 100, N)
    Yinit = np.random.uniform(-100, 100, N)

    #returns initial Utot and partial derivatives wrt to Dx and Dy
    Utot  = CoordsToPotential(Xinit, Yinit, a, b, N, Eye, Ones) 
    
    M3D = np.zeros((iterations, 3, N))
    M2D = np.zeros((3,N))

    
    for i in range(iterations):
        #generate potential new positions
        dx = step_size* np.random.choice([-1, 1],(N,))
        dy = step_size* np.random.choice([-1, 1],(N,))
        
        X_temp = Xinit + dx
        Y_temp = Yinit + dy

        #calculate Utot based on potential new positions
        Utot_temp = CoordsToPotential(X_temp, Y_temp, a, b, N, Eye, Ones)

        #difference between current and potential new Utot
        Utot_Diff = Utot - Utot_temp
        
        for j, u in enumerate(Utot_Diff):
            #if change in Utot is positive, determine if move happens
            if u <= 0:
                #calculate probability of move
                p_move = np.exp(-u/T)
                rho = np.random.uniform(0,1)
                
                if rho < p_move:
                    Xinit[j] = X_temp[j]
                    Yinit[j] = Y_temp[j]

            #if change in Utot is negative, allow move
            else:
                Xinit[j] = X_temp[j]
                Yinit[j] = Y_temp[j]
        
        #Calculate Utot after moves are complete
        Utot = CoordsToPotential(Xinit, Yinit, a, b, N, Eye, Ones) 
        
        
        M2D = np.array([Utot, Xinit, Yinit])
        M3D[i] = M2D

    return M3D


def plot_ParticleLocations(iterations, M3D, N):
    
    for i in range(iterations):

        if i == 0:
            plt.scatter(M3D[i,1,:], M3D[i, 2, :], alpha = 0.3)
            plt.xlim(-120, 120)
            plt.ylim(-120, 120)
            plt.title('initial conditions')
            plt.xlabel('x-plane position')
            plt.ylabel('y-plane position')
            plt.show()
        
        if i%100 == 0:
            
            plt.scatter(M3D[i,1,:], M3D[i, 2, :], alpha = 0.3)
            plt.xlim(-120, 120)
            plt.ylim(-120, 120)
            plt.title(f'Particle 2D Positions: {i}, Iterations, {N}, Particles')
            plt.xlabel('x-plane position')
            plt.ylabel('y-plane position')
            plt.show()



class LennardJones_Potential():
    
    def __init__(self, iterations = 100000, N = 200, a = 1, b = 1, T = 37.0, step_size = 0.03):
        
        self = self
        self.iterations = iterations
        self.N = N
        self.a = a
        
        self.Matrix = PotentialToMotion(iterations, N, a, b, T, step_size)
        
    def Plot_xy_Locations(self):
        plot_ParticleLocations(self.iterations, self.Matrix, self.N)
    


M = PotentialToMotion(iterations=10000, N=200, a=1.0, b=2.0, T=37.0, step_size = 0.3)
plot_ParticleLocations(100000, M, 200)

