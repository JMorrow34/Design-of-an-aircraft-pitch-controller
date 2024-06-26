# -*- coding: utf-8 -*-
"""coursework

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Gs55WvB2YHg3ivFgElZWti7D98kbMY1
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

alpha, r, delta, s, t, theta = sym.symbols('alpha, r, delta, s, t, theta')
d_psi_alpha= -0.31*alpha + 56.7*r + 0.231*delta
d_psi_alpha

Laplace_d_psi_alpha = sym.laplace_transform(d_psi_alpha,t,s)[0]
Laplace_d_psi_alpha

d_psi_r= - 0.014*alpha - 0.426*r + 0.0203*delta
d_psi_r

Laplace_d_psi_r = sym.laplace_transform(d_psi_r,t,s)[0]
Laplace_d_psi_r

d_psi_theta = 56.7*r
d_psi_theta

Laplace_d_psi_theta =sym.laplace_transform(d_psi_theta,t,s)[0]
Laplace_d_psi_theta

G_s = Laplace_d_psi_theta / Laplace_d_psi_alpha
G_s

"""Assuming zero initial conditions, after applying laplace transform to find the transfer function of the system. The following is derived."""