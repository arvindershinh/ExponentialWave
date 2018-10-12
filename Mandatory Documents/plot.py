# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 17:42:34 2018

@author: Arvinder Shinh
"""
import numpy as np
import matplotlib.pyplot as plt

# returns 10 evenly spaced samples from 0.1 to 2*PI
x = np.linspace(2, 2 * np.pi, 30)
G = np.zeros_like(x)
F = lambda x: np.exp(x)

fig, vax = plt.subplots(1, 1, figsize=(6, 3))
vax.plot(x, F(x), 'go', label='F(x)=exp(x)')
vax.plot(x, G, 'ro', label='G(x)=0')
vax.vlines(x, [0], F(x))
plt.legend()
plt.show()