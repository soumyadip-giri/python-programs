import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency
f = 5      # Frequency of the sine wave
T = 1      # Duration in seconds

# Generate sine wave
t = np.linspace(0, T, fs, endpoint=False)  # Time vector
signal = np.sin(2 * np.pi * f * t)         # Sine wave

# Plot original sine wave
plt.plot(t, signal)
plt.title("Original Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

# Compute and plot FFT frequency spectrum
fft_signal = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(len(signal), 1 / fs)
plt.plot(fft_freq[:fs // 2], np.abs(fft_signal)[:fs // 2])  # Only positive frequencies
plt.title("FFT Frequency Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.show()
