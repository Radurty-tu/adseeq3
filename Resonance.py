# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:47:59 2020

@author: mgerritsma
"""


import numpy as np
import matplotlib.pyplot as plt

L = 25e-6
C = 1e-9

f = np.linspace(1e-6,2,250)
omega = 2*np.pi*f*1e6

R = 20

T20 = 1/np.sqrt(R*R+(omega*L - (1/(omega*C)))*(omega*L - (1/(omega*C))))

R = 100
T100 = 1/np.sqrt(R*R+(omega*L - (1/(omega*C)))*(omega*L - (1/(omega*C))))

plt.plot(f,T20,label="R=20 $\Omega$")
plt.plot(f,T100,label="R=100 $\Omega$")
plt.xlabel('frequency [ 10^6 Hz]')
plt.legend()
plt.show()