# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:44:56 2018

@author: Arvinder Shinh
"""

import numpy as np
import matplotlib.pyplot as plt


p=lambda t: np.power(np.exp(2*t)+1,1/2)

ExLen = lambda t: p(t)+(1/2)*(np.log((p(t)-1)/(p(t)+1))-np.log((p(0)-1)/(p(0)+1)))-p(0)

m = lambda t: np.sin(ExLen(t))
#m = lambda t: np.sin(t)

n = lambda t: m(t)/p(t) 

def Y(t):
    return n(t)+np.exp(t)

def X(t):
    return -n(t)*np.exp(t)+t


t=np.linspace(-10, 3, 1000)
Z=X(t)+Y(t)*1j

fig0=plt.figure(figsize=(15,15))
ax=fig0.subplots(1,1)

ax.axvline()
ax.axhline()
ax.set_aspect('equal')
ax.plot(Z.real,Z.imag,'g.-')
ax.plot(t,np.exp(t),'y.-')
#ax.plot(t,np.sin(t), 'g.-')
#ax.plot(t,ExLen(t),'g.-')
#ax.plot(t,np.exp(t)+np.sin(10*t),'r.-')

    
    