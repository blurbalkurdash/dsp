import numpy as np
import matplotlib.pyplot as plt

#default constructor parameters
_F = 10000
_A = 1
_P = 0
_D = 1
_L = 1000000
_S = None

class Waveform:
    def __init__(self,frequency=_F,amplitude=_A,phase=_P,duration=_D,length=_L,sig=_S):
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
            self._w = 0
            self.t = np.linspace(0,duration,length)
            self.x = sig
    
    def fourier(self):
        spect = np.fft.fft(self.x)
        spect = spect/self._length
        magnitude = np.abs(spect)
        phase = np.angle(spect)
        return{'magnitude':magnitude,'phase':phase}
    
    def plot(self,num=5):
        plt.figure()
        plt.plot(self.t,self.x)
        try:
            plt.xlim(0,num/self._f)
        except ZeroDivisionError:
            pass
        
        plt.xlabel('Time [s]')
        plt.ylabel('Amplitude')
        plt.title('Time Series Data')
        
        return None

    def plot_spectrum(self):
        spect = self.fourier()
        y = spect['magnitude']
        y = y[0:int(self._length/2)]
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
class Sine_Wave(Waveform):
    def __init__(self,frequency=_F,amplitude=_A,phase=_P,duration=_D,length=_L):
        super().__init__(frequency,amplitude,phase,duration,length,None)
        self.x = amplitude * np.sin(self._w * self.t + phase)

class Square_Wave(Waveform):
    def __init__(self,frequency=_F,amplitude=_A,phase=_P,duration=_D,length=_L):
        super().__init__(frequency,amplitude,phase,duration,length,None)
        self.x = np.sign(np.sin(self._w * self.t + phase))
        
class Sawtooth_Wave(Waveform):
    def __init__(self,frequency=_F,amplitude=_A,phase=_P,duration=_D,length=_L):
        super().__init__(frequency,amplitude,phase,duration,length,None)
        self.x = 2*amplitude*((self.t*frequency + phase) - np.floor(self.t*frequency + phase) - 0.5)
        
class Triangle_Wave(Waveform):
    def __init__(self,frequency=_F,amplitude=_A,phase=_P,duration=_D,length=_L):
        super().__init__(frequency,amplitude,phase,duration,length,None)
        self.x = np.abs(2*amplitude*((self.t*frequency + phase) - np.floor(self.t*frequency + phase) - 0.5))

class Step(Waveform):
    def __init__(self,amplitude=_A,start=int(_L/2),length=_L):
        super().__init__(0,amplitude,0,1,length,None) 
        self.x = np.zeros(length)
        self.x[start:] = amplitude
        
class Ramp(Waveform):
    def __init__(self,amplitude=_A,rate=1,length=_L):
        super().__init__(0,amplitude,0,1,length,None)
        self.x = rate * self.t
        
class Hat(Waveform):
    def __init__(self,amplitude=_A,width=int(_L/3),start=int(_L/3),length=_L):
        if length < start + width:
            raise ValueError('signal length too short')
        super().__init__(0,amplitude,0,1,length,None)
        self.x = np.zeros(length)
        self.x[start:start+width] = amplitude