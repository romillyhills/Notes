#
# A script to calculate the first n energy levels of the hydrogen atom
#
import math


# declare constants

# mass of an electron
m_e = 9.109558*10**-31
# mass of a proton
m_p = 1.672614*10**-27
mu = m_e*m_p/(m_e+m_p)
# electric charge
ec = 1.60217662*10**-19
Q = -1*ec
q = 1*ec
# reduced plank contand
hbar = 1.0545718*10**-34
# permittivity of free space
epsilon_0 = 8.854187812813*10**-12

# declare equation for energy
E=-((Q**2)*(q**2)*mu)/(32*(hbar**2)*(math.pi**2)*epsilon_0**2)

# determine first n energy levels

for i in range(5):
    print((1/(i+1)**2)*E/ec)
    
# These results can be checked against
#
# https://astro.unl.edu/naap/hydrogen/transitions.html
# http://electron6.phys.utk.edu/phys250/modules/module%203/hydrogen_atom.htm
# https://en.wikipedia.org/wiki/Hydrogen_atom