import numpy as np
import matplotlib.pyplot as plt
## Parameters
fs = 1000 #Sampling frequency
f=5 #Frequency of the sine wave
T=1 # Duration in seconds
#Time vector
t = np.linspace(0, T, int(T* fs), endpoint=False)
# Generate sine wave
signal = np.sin(2* np.pi* f*t)
#This code generates a sine wave signal with a frequency of 5 Hz, sampled at 1000 Hz for 1 second.
#To plot the original sine wave:
plt.figure(figsize=(8, 4))
plt.plot(t, signal)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Original Sine Wave')
plt.tight_layout()
plt.show()
#This will display the original sine wave signal in the time domain.
#To compute and Plot the FFT Frequency Spectrum:
# Compute FFT
fft_signal = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(len(signal), 1/fs)
# Compute magnitude spectrum
magnitude_spectrum = np.abs(fft_signal)
#Plot the FFT frequency spectrum
plt.figure(figsize=(8, 4))
plt.plot(fft_freq, magnitude_spectrum)
plt.xlabel('Frequency [Hz]') 
plt.ylabel('Magnitude')
plt.title('FFT Frequency Spectrum')
plt.tight_layout()
plt.show()