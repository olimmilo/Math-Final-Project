 
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np
import random
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

def LinFit(xvalues, xrough, yrough):
	yvalues = []
	xpath = signal.find_peaks_cwt(yrough, np.arange(1,10))
	ypath = [yrough[x] for x in xpath]
	xpath.append(xvalues[-1])
	ypath.append(0)
	
	ysets = []
	
	ysetsfin = []
	
	i = 0
	j = 0
	while i < len(xpath):
		set = []
		while xvalues[j] <= xpath[i]:
			set.append(xvalues[j])
			j += 1
		ysets.append(set)
		i += 1
	i = 0
	
	while i < len(ysets):
		regression = np.polyfit([xpath[i-1], xpath[i]],[ypath[i-1], ypath[i]],1)
		ysetsfin.append(Fit(regression, ysets[i]))	
		i += 1
	
	i = 0
	
	yvalues = [p for q in ysetsfin for p in q]
	
	if len(xvalues) == len(yvalues):
		print('yay')
	
	return(yvalues)

def Final(xvalue,frequency,amplitude):
	i = 0
	yvalue = 0
	while i < len(frequency):
		yvalue += amplitude*np.sin(x*frequency+(random.uniform(0,0.5)-0.25))
		i += 1
	i = 0
	return(yvalue)

soundA, samplerateA = sf.read(RAWSOUNDFILE)
soundAy = soundA
soundAx = [x/1000 for x in range(len(soundAy))]

fftA = fft(soundA)
fftAy = [np.abs(x) for x in fftA[:10000]]
fftAx = [x for x in range(10000)]

maxAx = signal.find_peaks_cwt(fftAy[:2000], np.arange(1,10))
maxAy = [fftAy[x] for x in maxAx]

ampAx = soundAx
ampAy = [(np.abs(x)) for x in soundAy]
pol = 4
reg =  np.polyfit(ampAx, ampAy, pol)
ampBx = ampAx 
ampBy = Fit(reg, ampBx)
ampCx = ampBx
ampCy = LinFit(ampCx, soundAx, soundAy)

compAx = soundAx
compAy = [Final(x,maxAx,maxAy)*ampCy[x] for x in compAx]

plt.figure(1)
plt.plot(soundAx, soundAy)
plt.plot(ampBx, ampBy)
plt.plot(ampCx, ampCy)
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

plt.figure(3)
plt.plot(compAx, compAy)
plt.xlabel('Time')
plt.ylabel('Air Pressure Variation')
plt.title('Final Constructed Composite Soundwave')

plt.show()
