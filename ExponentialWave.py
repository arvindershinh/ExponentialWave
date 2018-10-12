# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:44:56 2018

@author: Arvinder Shinh
"""

import numpy as np
import matplotlib.pyplot as plt

G=lambda t: np.exp(t)

P=lambda t: np.power(np.exp(2*t)+1,1/2)

Length_G = lambda t: +P(t)+(1/2)*(np.log((P(t)-1)/(P(t)+1)))-P(0)-(1/2)*(np.log((P(0)-1)/(P(0)+1)))

F = lambda t: np.sin(t)

X = lambda t: -(F(Length_G(t))/P(t))*np.exp(t)+t
Y = lambda t: +(F(Length_G(t))/P(t))+np.exp(t)

t=np.linspace(-10, 3, 2000)
Z=X(t)+Y(t)*1j

fig0=plt.figure(figsize=(15,15))
ax=fig0.subplots(1,1)

ax.axvline()
ax.axhline()
ax.set_aspect('equal')
ax.plot(Z.real,Z.imag,'g.-')
ax.plot(t,np.exp(t))
#ax.plot(t,np.sin(t), 'g.-')
#ax.plot(t,ExLen(t),'g.-')
#ax.plot(t,np.exp(t)+np.sin(10*t),'r.-')

    
    