import matplotlib.pyplot as plt #imports packages used to allow the code to produce graphs
import soundfile as sf #imports packages used to allow the code to understand soundfiles
import numpy as np #adds extra math functionality
from scipy.fftpack import fft #imports a fourier algorithm
from scipy import signal #signal proscessing functionality

"""
Initially Defined Functions
"""

def SoundProscessing(init_sound_list):
	final_y = []
	final_x = []
	i = 0
	while i < len(init_sound_list[1]):
		if init_sound_list[1][i] > 0:
			value_y = init_sound_list[1][i]
			value_x = init_sound_list[0][i]
			final_y.append(value_y)
			final_x.append(value_x)
		i += 1
	final = [final_x, final_y]
	return(final)

def QuarticRegression(init_sound_list,raw_sound_list):
	reg = np.polyfit(init_sound_list[0], init_sound_list[1], 4)
	final_x = raw_sound_list[0]
	final_y = [((reg[0]*(x**4))+(reg[1]*(x**3))+(reg[2]*(x**2))+(reg[3]*x)+reg[4]) for x in final_x]
	final = [final_x, final_y]
	return(final)
	
def SoundComposition(init_tone_list,regression_list):
	tone_x = init_tone_list[0]
	tone_y = []
	i = 0
	while i < len(tone_x):
		value = init_tone_list[1][i]*regression_list[1][i]
		tone_y.append(value)
		i += 1
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

proc = [np.abs(sound_raw[1][x]) for x in range(len(sound_raw[1]))]

sound_proc = [sound_raw[0], proc]

raw_max_x = signal.find_peaks_cwt(sound_proc[1], np.arange(1,10))
raw_max_y = [sound_raw[1][x] for x in raw_max_x]
raw_max = [raw_max_x, raw_max_y]

processed_sound = SoundProscessing(raw_max)

#finds the  quartic amplitude function

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

fft_max_x = signal.find_peaks_cwt(fft[1][:3500], np.arange(20,200))
fft_max_y = [fft[1][x] for x in fft_max_x]
fft_max = [fft_max_x, fft_max_y]

"""
#Part Three
"""

#Creates a list of each individual pure tone

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

#Sums the pure tones into a composite tone

fin_tone_x = sound_raw[0]
fin_tone_y = [0 for x in fin_tone_x]
i = 0
while i < len(pure_tones):
	fin_tone_y = [fin_tone_y[x]+pure_tones[i][1][x] for x in range(len(fin_tone_x))]
	i += 1
fin_tone = [fin_tone_x, fin_tone_y]

#combines pure tones and amplitude function into in composite sound wave


comp_quart = SoundComposition(fin_tone, reg_quart)

"""
#Graphing
"""

#Graphs the raw soundwave against the amplitude function


plt.figure(1)
plt.plot(sound_raw[0], sound_raw[1])
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

#Graphs the composite wave forms using the amplitude function

plt.figure(3)
plt.plot(comp_quart[0], comp_quart[1])
plt.xlabel('Time')
plt.ylabel('Air Pressure Variation')
plt.title('Final Constructed Composite Soundwave')

#shows the graphs

plt.show()

