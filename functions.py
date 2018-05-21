from pydub import AudioSegment

FILENAEMIN = "trial1.mp3"
FILENAMEOUT = "trial1"

INSTRUMENTLIBRARY = [] ## [[name, [data per milisecond]],[name, [data per milisecond]]]

FILETYPE=[wav,mp3,ogg,flv]

def InputSound(namein,nameout,filetype): ##filetype is the integer relating to the file
	
	error = 0
	
	"""
	checks name error
	"""
	
	namelist = []
	i = 0
	while i < len(INSTRUMENTLIBRARY):
		namelist.append(INSTRUMENTLIBRARY[i][1])
		i += 1
	i = 0
	
	while i < len(namelist):
		if namelist[i] == nameout:
			error = 1
		i += 1
	i = 0
	
	if error = 0:
		return("ERROR 1")
		break
		
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
		return("ERROR 2")
		break
	output = [nameout, rawaudio]
	
	return(output)
