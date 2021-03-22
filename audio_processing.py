import librosa, librosa.display
import matplotlib.pyplot as plt

x="s2.wav"                   # audio source 
audio, sr = librosa.load(x)  # sr = sample rate (no. of amplitude values per sec)
                             # audio = gives all amplitude values in the form of an array


# plottin audio amplitude vs time
plt.figure(figsize=(10,5))
librosa.display.waveplot(audio)  
plt.title("audio")
plt.ylim((-1,1))
plt.show()
