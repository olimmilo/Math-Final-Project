 
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np
from scipy.fftpack import fft
from scipy import signal


RAWSOUNDFILE = 'sound-a.wav'

def Fit(lista, listb):
    output = []
    i = 0
    while i < len(listb):
        j = 0
        j1 = len(lista)-1
        final = 0
        while j < len(lista):
            final += lista[j]*listb[i]**j1
            j += 1
            j1 = j1-1
        output.append(final)
        i += 1
    i = 0
    return(output)

soundA, samplerateA = sf.read(RAWSOUNDFILE)
soundAy = soundA
soundAx = [x/1000 for x in range(len(soundAy))]

fftA = fft(soundA)
fftAy = [np.abs(x) for x in fftA[:10000]]
fftAx = [x for x in range(10000)]

#maxA1 = signal.find_peaks_cwt(fftAy[:2000], np.arange(1,10))
#maxA2 = signal.find_peaks_cwt(fftAy[2000:], 1000)
#maxAy = maxA1y+maxA2y

maxAx = signal.find_peaks_cwt(fftAy[:2000], np.arange(1,10))
maxAy = [fftAy[x] for x in maxAx]

ampAx = soundAx
ampAy = [(np.abs(x)) for x in soundAy]
pol = 4
reg =  np.polyfit(ampAx, ampAy, pol)
ampBx = ampAx 
ampBy = Fit(reg, ampBx)

plt.figure(1)
plt.plot(soundAx, soundAy)
plt.plot(ampBx, ampBy)
plt.xlabel('Time')
plt.ylabel('Air Pressure Variation')
plt.title('Recorded Composite Soundwave')


plt.figure(2)
plt.hold(True)
plt.plot(fftAx, fftAy)
plt.scatter(maxAx, maxAy, c='red')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Fourier Transform of Recorded Soundwave')

"""
plt.figure(4)
plt.plot(compAx, compAy)
plt.xlabel('Time')
plt.ylabel('Air Pressure Variation')
plt.title('Final Constructed Composite Soundwave')
"""

plt.show()
