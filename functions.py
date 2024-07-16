import numpy as np

G = 6.67e-11 #Newtons kg-2 m2.
c = 299792458 #m/s
Msun = 1.989e30 #kg

# gravitational radius
def rg(mass):
    return G*mass/c**2

# Schwarzschild radius / event horizon radius
rs = 2 * rg

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