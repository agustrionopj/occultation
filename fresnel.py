# -*- coding: utf-8 -*-
"""
Edited on Thu May 11, 2017

@author: PJ
"""

from pylab import *
from scipy.special import fresnel
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

pjgGel, weight1, weight2 = loadtxt('transcurveb.txt', unpack=True)

x = np.linspace(-100., 100., 50000)

pjgGel_weight = pjgGel * weight1

pjgGel_tes = 15000.

n = len(x)
m = len(pjgGel_weight)

result1 = zeros((n, m))      # nrows, ncols --> kebalikan dari IDL
result2 = zeros((n, m))

for i in range (m):
    for j in range (n):
        w1 = x[j] * 1e10 * sqrt(2. / (pjgGel_weight[i] * 3.84e18))
        w2 = x[j] * 1e10 * sqrt(2. / (pjgGel_tes * 3.84e18))
        s1, c1 = fresnel(w1)
        s2, c2 = fresnel(w2)
        result1[j, i] = 0.5 * (0.5 + s1 + 0.5 + c1) ** 2
        result2[j, i] = 0.5 * (0.5 + s2 + 0.5 + c2) ** 2
total_res1 = result1.sum(axis = 1)
total_res2 = result2.sum(axis = 1)

plt.plot(x, total_res1)
plt.plot(x, total_res2)
plt.grid(True)
plt.show()

# x_data, y_data = loadtxt('data_LO.txt', unpack=True) # buka file masukan
# plt.plot(x_data, y_data, 'ro') #plot file masukan
# plt.show()

