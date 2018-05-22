from pydub import AudioSegment

FILENAEMIN = "trial1.mp3"
FILENAMEOUT = "trial1"

INSTRUMENTLIBRARY = [] ## [[name, [data per milisecond]],[name, [data per milisecond]]]

FILETYPE=['wav','mp3','ogg','flv']

def Mean(data):
	sum = 0
	i = 0
	
	while i < len(data):
		sum += data[i]
		i += 1
	
	mean = sum/len(data)
	return(mean)

def InputSound(namein,nameout,filetype,instrumentlibrary): ##filetype is the integer relating to the file
	
	error = 0
	
	"""
	checks name error
	"""
	
	namelist = []
	i = 0
	while i < len(instrumentlibrary):
		namelist.append(instrumentlibrary[i][1])
		i += 1
	i = 0
	
	while i < len(namelist):
		if namelist[i] == nameout:
			error = 1
		i += 1
	i = 0
		
	"""
	opens file and turns it to raw data 
	"""
	
	if filetype == 0:
		rawaudio = AudioSegment.from_wav(namein)
	elif filetype == 1:
		rawaudio = AudioSegment.from_mp3(namein)
	elif filetype == 2:
		rawaudio = AudioSegment.from_ogg(namein)
	elif filetype == 3:
		rawaudio = AudioSegment.from_flv(namein)
	else:
		error = 2
	
	mean = Mean(rawaudio)
	
	equalizedaudio = []
	
	i = 0
	
	while i < len(rawaudio):
		equalizedaudio.append(rawaudio[i]-mean)
		i += 1
	
	i = 0
	
	output = [nameout, equalizedaudio]
	if error == 1:
		return("ERROR 1")
    elif error == 2:
        return("ERROR 2")
    else:
        return(output)
