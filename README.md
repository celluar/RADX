# RAD-X
Relativistic Accretion Disk - X
Corrective code for disk spectrum applying doppler shift and relativistic effects using iron lines.

Energy shift in a BH accretion disk in the Schwarzschild metric following Poutanen+2020


Disk surface element at radius $R$ is moving with Keplerian velocity $\mathbf{v}= v \cdot (-\sin{\varphi}, \; \cos{\varphi}, \; 0)$ with $\beta = v/c = \sqrt{u/2(1-u)}$ relative to a static observer at this radius (see, e.g. Luminet 1979).

Photon momentum makes angle $\xi$ with the velocity vector (eq. 26)
$$
\cos{\xi} = \mathbf{\hat{v}} \cdot \mathbf{\hat{k}}_0 = \frac{\sin{\alpha}}{\sin{\psi}} \mathbf{\hat{v}} \cdot \mathbf{\hat{o}} = - \frac{\sin{\alpha}}{\sin{\psi}} \sin{i} \sin{\varphi}
$$
and it makes angle $\zeta$ with the local disk normal:
$$
\cos{\zeta} = \mathbf{\hat{n}} \cdot \mathbf{\hat{k}}_0 = \frac{\sin{\alpha}}{\sin{\psi}} \mathbf{\hat{n}} \cdot \mathbf{\hat{o}} = \frac{\sin{\alpha}}{\sin{\psi}} \cos{i}
$$


Doppler factor (eq. 28)
$$
\delta = \frac{1}{\gamma (1- \mathbf{\hat{\beta}} \cdot \mathbf{\hat{k}}_0)} = \frac{1}{\gamma (1-\beta \cos \xi)}
$$

Corresponding Lorentz factor

$$
\gamma = \frac{1}{\sqrt{1-\beta^2}} = \sqrt{\frac{1-u}{1-3u/2}}
$$

Energy ratio (Poutanen2020 eq. 32, adapted from Luminet1979 and Chen+1989)
$$
\frac{E}{E'} = \delta \sqrt{1-u} = \frac{\sqrt{1-3u/2}}{1+\beta \sin{i} \sin{\varphi} \sin{\alpha}/\sin{\psi}}
$$
combines the effects of the gravitational redshift and Doppler effect

# HOW TO USE 
Install RADX by using 

        pip install RADX            
First, import RADX and its functions

        from RADX import radx_functions as radx_func



