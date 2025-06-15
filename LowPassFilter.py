# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:52:17 2020

@author: mgerritsma
"""

import numpy as np
import matplotlib.pyplot as plt
import array as arr

R = 850
C = 1e-6
Hlow = []
Hhigh = []
fp = []
philow = []
phihigh = []

f = np.linspace(1e1,1e4,500)
omega = arr.array('d',2*np.pi*f)

for i in range(len(omega)):
    temp = 1/np.sqrt(1+omega[i]*omega[i]*R*R*C*C)
    temp2 = omega[i]*R*C/np.sqrt(1+omega[i]*omega[i]*R*R*C*C)
    ftemp = f[i]
    fp.append(ftemp)
    Hlow.append(temp)
    Hhigh.append(temp2)
    philow.append((180/np.pi)*np.arctan(-omega[i]*R*C))
    phihigh.append((180/np.pi)*np.arctan(1/(omega[i]*R*C)))
    
plt.figure(1)
plt.title('Low-pass RC')  
plt.loglog(fp,Hlow)
plt.xlabel('frequency [Hz]')
plt.ylabel('|H(f)| [dB]')
plt.xlim([1e1, 1e4])
plt.grid()
plt.show()

plt.figure(2)
plt.title('High-pass RC')  
plt.loglog(fp,Hhigh)
plt.xlabel('frequency [Hz]')
plt.ylabel('|H(f)| [dB]')
plt.xlim([1e1, 1e4])
plt.grid()
plt.show()

plt.figure(3)
plt.plot(fp,philow)
plt.xscale('log')
plt.xlabel('frequency [Hz]')
plt.ylabel('phase [degrees]')
plt.xlim([1e1, 1e4])
plt.ylim([-100,100])
plt.grid()
plt.show()

plt.figure(4)
plt.plot(fp,phihigh)
plt.xscale('log')
plt.xlabel('frequency [Hz]')
plt.ylabel('phase [degrees]')
plt.xlim([1e1, 1e4])
plt.ylim([-100,100])
plt.grid()
plt.show()

    