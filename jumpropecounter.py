import sounddevice as sd
import datetime as dt
import time 
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 0.1 # Duration of recording
while(1):
	skips =0
	start=0
	silence=0
	beg=0
	while(1):
		count=skips
		cross=0
		sound = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
		sd.wait()  # Wait until recording is finished
		for i in range(0,sound.size):
			if(sound[i]>=0.095):
				cross=cross+1
				silence=0
				if(start==0):
					beg=int(dt.datetime.now().second)+int(dt.datetime.now().minute)
					start=1
			if(cross<30 and cross>0):
				skips=skips+1
			break




		if(count==skips):
			silence=silence+1
		if(silence==16):
			if(skips!=0):
				print("total jumps : ",skips,"\n")
				print("time in minutes : ",int(((int(dt.datetime.now().second)/60+int(dt.datetime.now().minute))-beg)),"\n")
				print("approx calories burned  : ",int(((int(dt.datetime.now().second)/60+int(dt.datetime.now().minute))-beg)*14.7),"\n")
			break







