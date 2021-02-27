import librosa, librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np

x="s2.wav"
x1, sr =librosa.load(x)
print(x1.size)

plt.figure(figsize=(15,17))
plt.subplot(3,1,1)
librosa.display.waveplot(x1)
plt.title("x1")
plt.ylim((-1,1))
plt.show()