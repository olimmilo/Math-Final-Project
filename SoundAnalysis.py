import matplotlib.pyplot as plt #imports packages used to allow the code to produce graphs
import soundfile as sf #imports packages used to allow the code to understand soundfiles
import numpy as np #adds extra math functionality
from scipy.fftpack import fft #imports a fourier algorithm
from scipy import signal #signal proscessing functionality

"""
Initially Defined Functions
"""

def SoundProscessing(init_sound_list):
	final = init_sound_list
	return(final)

def LinearRegression(init_sound_list,raw_sound_list):
	final_x = raw_sound_list[0]
	#trial: y = 1/100000xx + .1
	final_y = [((1/100000)*x)+.1 for x in final_x]
	final = [final_x, final_y]
	return(final)

def QuarticRegression(init_sound_list,raw_sound_list):
	final_x = raw_sound_list[0]
	#trial: y = 1/2000000 + .05
	final_y = [((1/200000)*x)+.05 for x in final_x]
	final = [final_x, final_y]
	return(final)
	
def SoundComposition(init_tone_list,regression_list):
	tone_x = init_tone_list[0]
	tone_y = [init_tone_list[1][x]*regression_list[1] for x in range(len(tone_x))]
	tone = [tone_x, tone_y]
	return(tone)

"""
PART ONE
"""

#imports the raw sound and turns it into workable data

sound_raw_y, sample_rate = sf.read('raw-sound.wav') #sound file contained in the same directory in which the program is run

sound_raw_x = [x for x in range(len(sound_raw_y))]

sound_raw = [sound_raw_x, sound_raw_y]

#converts the raw sound into a proscessed form which can be used to find the amplitude functions

processed_sound = SoundProscessing(sound_raw)

#finds the linear and quartic amplitude functions

reg_lin = LinearRegression(processed_sound,sound_raw)
reg_quart = QuarticRegression(processed_sound,sound_raw)



"""
#PART TWO
"""

#uses the FFT algoritm to proscess the raw sound into its component pure tones and amplitudes therein

fft_raw = fft(sound_raw[1])
fft_y = [np.abs(x) for x in fft_raw[:10000]]
fft_x = [x for x in range(len(fft_y))]
fft = [fft_x, fft_y]

#finds the local maxima of the FFT function to determine the discrete component pure tones

fft_max_x = signal.find_peaks_cwt(fft[1], np.arange(1,10))
fft_max_y = [fft[1][x] for x in fft_max_x]
fft_max = [fft_max_x, fft_max_y]

"""
#Part Three
"""

#Creates a list of each individual pure tone

'''
pure_tones = []
i = 0
while i < len(fft_max[0]):
	tone_x = sound_raw[0]
	freq = fft_max[0][i]
	amp = fft_max[1][i]
	tone_y = []
	j = 0
	while j < len(tone_x):
		value = amp*np.sin(tone_x[j]*freq)
		tone_y.append(value)
		j += 1
	tone = [tone_x, tone_y]
	pure_tones.append(tone)
	i += 1
i = 0
'''
#Sums the pure tones into a composite tone

#combines pure tones and amplitude functions into in composite sound wave

comp_lin = SoundComposition(sound_raw, reg_lin)
comp_quart = SoundComposition(sound_raw, reg_quart)

"""
#Graphing
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
plt.plot(fft[0], fft[1], zorder=1)
plt.scatter(fft_max[0], fft_max[1], c='red', marker='d',zorder=2)
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

