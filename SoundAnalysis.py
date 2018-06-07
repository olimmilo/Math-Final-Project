import matplotlib.pyplot as plt #imports packages used to allow the code to produce graphs
import soundfile as sf #imports packages used to allow the code to understand soundfiles
import numpy as np #extra math functionality
from scipy.fftpack import fft #imports a fourier algorithm
from scipy import signal #signal proscessing functionality

"""
Initially Defined Functions
"""

def SoundProscessing(init_sound_list):
	pass

def LinearRegression(init_sound_list):
	pass

def QuarticRegression(init_sound_list):
	pass
	
def Sound_composition(pure_tones,regression)
	pass

"""
PART ONE
"""

#imports the raw sound and turns it into workable data

#converts the raw sound into a proscessed form which can be used to find the amplitude functions

#finds the linear and quartic amplitude functions

"""
PART TWO
"""

#uses the FFT algoritm to proscess the raw sound into its component pure tones and amplitudes therein

#finds the local maxima of the FFT function to determine the discrete component pure tones

"""
Part Three
"""

#Creates a list of each individual pure tone

#combines pure tones and amplitude functions into in composite sound wave

"""
Graphing
"""

#Graphs the raw soundwave against the two amplitude functions

plt.figure(1)
plt.plot(sound_raw[0], sound_raw[1])
plt.plot(reg_lin[0], reg_lin[1])
plt.plot(reg_quart[0], reg_quart[1])
plt.xlabel('Time')
plt.ylabel('Air Pressure Variation')
plt.title('Recorded Composite Soundwave')

#Graphs the Fourier Transform of the raw sound wave against a scatter plot of the discretely selected frequencies

plt.figure(2)
plt.hold(True)
plt.plot(fft[0], fft[1])
plt.scatter(fft_max[0], fft_max[1], c='red')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Fourier Transform of Recorded Soundwave')

#Graphs the composite wave forms using the two different amplitude functions

plt.figure(3)
plt.subplot(comp_lin[0], comp_lin[1])
plt.subplot(comp_quart[0], comp_quart[1])
plt.xlabel('Time')
plt.ylabel('Air Pressure Variation')
plt.title('Final Constructed Composite Soundwaves')

#shows the graphs

plt.show()
