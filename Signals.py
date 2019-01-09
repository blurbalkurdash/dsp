import numpy as np
import matplotlib.pyplot as plt

#signal information
f = 1000 #Hz signal Frequency
w = 2*np.pi*f #angular frequency
T = 1/f #period
A = 1 #amplitude
phase = 0 #phase angle (rad)
duration = 0.1
start_time = 0

Fs = 7000#sampling frequency


t = np.linspace(start_time,start_time + duration, Fs*duration)
y = A*np.sin(w*t + phase)



#sampling information