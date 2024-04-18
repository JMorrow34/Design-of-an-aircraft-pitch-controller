# -*- coding: utf-8 -*-
"""final graphs

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KCjRkL0VNwCn1ZIFiteeNiY35nKMoYMt
"""

!pip install control numpy matplotlib

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

numerator = [1.151 , 0.1774]
denominator = [1, 0.739, 0.921]

sys = ctrl.TransferFunction(numerator, denominator)

plt.figure(figsize=(8, 6))
ctrl.bode_plot(sys, dB=True)
plt.grid(True)
plt.title('Bode Plot')
plt.show()

zeros = np.roots(numerator)
poles = np.roots(denominator)

print("Poles of the transfer function:", poles)
print("Zeros of the transfer function:", zeros)

plt.figure(figsize=(8, 6))
t, y = ctrl.step_response(sys)
plt.plot(t, y)
plt.grid(True)
plt.title('Step Response')
plt.xlabel('Time (sec)')
plt.ylabel('Response')
plt.show()

plt.figure(figsize=(8, 6))
t, y = ctrl.impulse_response(sys)
plt.plot(t, y)
plt.grid(True)
plt.title('Impulse Response')
plt.xlabel('Time (sec)')
plt.ylabel('Response')
plt.show()