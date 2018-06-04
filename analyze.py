 
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np
from scipy.fftpack import fft


RAWSOUNDFILE = 'sound-a.wav'

soundA, samplerateA = sf.read(RAWSOUNDFILE)
soundAy = soundA
soundAx = [x/1000 for x in range(len(soundAy))]

fftA = fft(soundA)
fftAy = [np.abs(x) for x in fftA[:10000]]
fftAx = [x for x in range(10000)]

plt.figure(1)
plt.plot(soundAx, soundAy)
plt.xlabel('Time')
plt.ylabel('Air Pressure Variation')
plt.title('Recorded Composite Soundwave')


plt.figure(2)
plt.plot(fftAx, fftAy)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Fourier Transform of Recorded Soundwave')

plt.figure(3)
plt.plot(ampAx, ampAy)
plt.plot(ampBx, ampBy)
plt.xlabel('Time')
plt.ylabel('Air Pressure Variation')
plt.title('Amplitude over Time')

plt.figure(4)
plt.plot(wavAx, wavAy)
plt.xlabel('Time')
plt.ylabel('Air Pressure Variation')
plt.title('Selected Waves')

plt.figure(5)
plt.plot(compAx, compAy)
plt.xlabel('Time')
plt.ylabel('Air Pressure Variation')

plt.title('Final Constructed Composite Soundwave')

plt.show()
