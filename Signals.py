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

class Waveform:
    def __init__(self,frequency=1000,amplitude=1,phase=0,duration=1,length=5000,sig=None):
        if sig is None:
            self._f = frequency
            self._phase = phase
            self._amplitude = amplitude
            self._length = length
            self._w = 2*np.pi*frequency
            self.t = np.linspace(0,duration,length)
            self.x = [self._amplitude for timestep in self.t]
        else:
            self._f = 0
            self._phase = 0
            self._amplitude = 0
            self._length = len(sig)
            self._w = 2*np.pi*frequency
            self.t = np.linspace(0,duration,length)
            self.x = sig
    
    def fourier(self):
        spect = np.fft.fft(self.x)
        spect = spect/self._length
        magnitude = np.abs(spect)
        phase = np.angle(spect)
        return{'magnitude':magnitude,'phase':phase}
    
    def plot(self):
        plt.figure()
        plt.plot(self.t,self.x)
        plt.xlabel('Time [s]')
        plt.ylabel('Amplitude')
        plt.title('Time Series Data')
        
        return None

    def plot_spectrum(self):
        spect = self.fourier()
        y = spect['magnitude']
        y = y[0:int(self.length)/2]
        y[1:] = 2*y[1:]
        f = 48000 * np.arange(len(self.t)/2)/len(self.t)
        plt.figure()
        plt.plot(f,y)
        plt.xlabel('Frequency [hz]')
        plt.ylabel('Amplitude')
        plt.title('Frequency Spectrum Magnitudes')
        plt.show()
        return None
    
   #TODO: implement specialized waveform subclasses



#sampling information