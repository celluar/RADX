
G = 6.67e-11 #Newtons kg-2 m2.
c = 299792458 #m/s
Msun = 1.989e30 #kg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


class Disk(object):

    def __init__(self,spin,inclination):
        self.BH_spin = spin
        self.rg = 1
        self.rs = 2*self.rg
        self.i = inclination
    
    
    def rms(self): 
        '''
    spin here is the unitless -1<a<1 value
    output in units of rg
        '''
        z1 = 1 + (1 - self.spin**2)**(1/3) * ((1 + self.spin)**(1/3) + (1 - self.spin)**(1/3))
        z2 = np.sqrt(3 * self.spin**2 + z1**2)
        r_ms_temp = (3 + z2 + np.sign(-self.spin) * np.sqrt( (3 - z1) * (3 + z1 + 2*z2) ) )
        
        self.r_ms = r_ms_temp(self.spin)
    
    def energy_shift(self,r,phi):
        u = self.rs/r
        beta = np.sqrt(u/(2*(1-u)))

        psi = np.arccos(np.sin(self.i) * np.cos(phi))

        alpha = np.arccos(1-(1-u)*(1-np.cos(psi)))

        xi = np.arccos(- np.sin(alpha)/np.sin(psi) * np.sin(self.i)*np.sin(phi))
        zeta = np.arccos(np.sin(alpha)/np.sin(psi) * np.cos(self.i))

        num = np.sqrt(1 - 3*u/2)
        den = 1+ beta * np.sin(self.i) * np.sin(phi) * np.sin(alpha) / np.sin(psi)
        return num/den
    
    def diskeq(self,r,theta):
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        z = self.energy_shift(r,theta)
        return x,y,z
    
    def plot_disk(self):
        r=np.linspace(5, 30)
        phi=np.linspace(0, 2*np.pi) 
        R,T = np.meshgrid(r,phi)
        X,Y,Z = self.diskeq(R,T)

        # make the surface plot
        fig = plt.figure(figsize=(12,8))           # get a new figure
        ax = fig.add_subplot(111,projection='3d')  # get some 3D axes in the figure
        plt.rc('font', size=12)
        ax.plot_surface(X,Y,Z,cmap=cm.plasma)  # do the surface plot
        ax.set_zlim(-4., 4.)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.title (r'Suface Plot')

        #elevate axis to viewer
        ax.view_init(elev=30,azim=0)
        plt.show()

