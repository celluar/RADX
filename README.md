# RAD-X
Relativistic Accretion Disk - X
Corrective code for disk spectrum applying doppler shift and relativistic effects using iron lines.

Line profile from a BH accretion disk in the Schwarzschild metric following Poutanen+2020




Photon momentum makes angle $\xi$ with the velocity vector
$$
\cos{\xi} = \mathbf{\hat{v}} \cdot \mathbf{\hat{k}}_0 = \frac{\sin{\alpha}}{\sin{\psi}} \mathbf{\hat{v}} \cdot \mathbf{\hat{o}} = - \frac{\sin{\alpha}}{\sin{\psi}} \sin{i} \sin{phi}
$$

Doppler factor
$$
\delta = \frac{1}{\gamma (1- \mathbf{\beta} \cdot \mathbf{\hat{k}}_0)} = \frac{1}{\gamma (1-\beta \cos \xi)}
$$

Energy ratio (Poutanen2020 eq. 32, adapted from Luminet1979 and Chen+1989)

$$
\frac{E}{E'} = \delta \sqrt{1-u} = \frac{\sqrt{1-3u/2}}{1+\beta \sin{i} \sin{\phi} \sin{\alpha}/\sin{\psi}}
$$

combines the effects of the gravitational redshift and Doppler effect