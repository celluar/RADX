import numpy as np
import matplotlib.pyplot as plt

G = 6.67e-11 #Newtons kg-2 m2.
c = 299792458 #m/s
Msun = 1.989e30 #kg

a = 0.998 # maximally spinning BH

# gravitational radius
#rg= G*mass/c**2
rg=1.

# Schwarzschild radius / event horizon radius
rs = 2 * rg
i=30 * np.pi/180

#  Radius of Marginal Stability (or isco for rotating BH)
def rms(spin): 
    '''
    spin here is the unitless -1<a<1 value
    output in units of rg
    '''
    z1 = 1 + (1 - spin**2)**(1/3) * ((1 + spin)**(1/3) + (1 - spin)**(1/3))
    z2 = np.sqrt(3 * spin**2 + z1**2)
    r_ms = (3 + z2 + np.sign(-spin) * np.sqrt( (3 - z1) * (3 + z1 + 2*z2) ) )
    return r_ms

r_ms = rg * rms(spin=a)

r=np.linspace(r_ms, 30 * rg)
phi=np.linspace(0, 2*np.pi)

u = rs/r
# Energy ratio (Poutanen eq. 32, adapted from Luminet1979, Chen+1989)

def energy_shift(u,phi):
    num = np.sqrt(1 - 3*u/2)
    den = 1+ beta * np.sin(i) * np.sin(phi) * np.sin(alpha) / np.sin(psi)
    return num/den


beta = np.sqrt(u/(2*(1-u)))
   
psi = np.arccos(np.sin(i) * np.cos(phi))

alpha = np.arccos(1-(1-u)*(1-np.cos(psi)))

xi = np.arccos(- np.sin(alpha)/np.sin(psi) * np.sin(i)*np.sin(phi))
zeta = np.arccos(np.sin(alpha)/np.sin(psi) * np.cos(i))

plt.plot(phi, energy_shift(5,phi))
plt.show()
