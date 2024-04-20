"""
OnOffKeying.py

This program generates a square wave, modulates it onto a carrier wave, 
demodulates the signal, and prints the demodulated signal.

Usage:
- Demonstrates the use of on off keying for modulation and demodulation.

Dependencies:
- numpy
- matplotlib
- csv

@author: Aryan Bansal
@date: 25th April 2024
@version: 1.0
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
from scipy.signal import medfilt

def generateSignal(frequency=2, duration=1, sampling_rate=1000):
    """
    Function to generate a digital signal.

    Args:
        frequency (float): Frequency of the digital signal.
        duration (float): Duration of the signal in seconds.
        sampling_rate (int): Sampling rate in Hz.

    Returns:
        t (numpy.ndarray): Time array.
        square_wave (numpy.ndarray): Generated square wave signal.
    """
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    square_wave = 0.5 * signal.square(2 * np.pi * frequency * t) + 0.5

    return t, square_wave

def modulateSignal(t, square, carrier_frequency=10):
    """
    Function to modulate the digital signal with a carrier wave.

    Args:
        t (numpy.ndarray): Time array.
        square (numpy.ndarray): digital signal.
        carrier_frequency (float): Frequency of the carrier wave.

    Returns:
        carrier_wave (numpy.ndarray): Carrier wave.
        modulated_signal (numpy.ndarray): Modulated signal.
    """
    carrier_wave = np.sin(2 * np.pi * carrier_frequency * t)
    modulated_signal = carrier_wave * square

    return carrier_wave, modulated_signal

def addNoise(modulated_signal, noise_amplitude=0.05):
    """
    Function to add Gaussian noise to the modulated signal.

    Args:
        modulated_signal (numpy.ndarray): Modulated signal.
        noise_amplitude (float): Amplitude of the Gaussian noise.

    Returns:
        noise (numpy.ndarray): Generated Gaussian noise.
        noisy_signal (numpy.ndarray): Modulated signal with added noise.
    """
    noise = np.random.normal(0, noise_amplitude, len(modulated_signal))
    noisy_signal = modulated_signal + noise

    return noise, noisy_signal

def demodulateSignal(modulatedSignal, windowSize=13):
    """
    Function to demodulate the modulated signal.

    Args:
        modulatedSignal (numpy.ndarray): Modulated signal.
        windowSize (int): Size of the median filter window.

    Returns:
        smoothed_signal (numpy.ndarray): Demodulated signal.
    """
    demodulatedData = []
    for sample in modulatedSignal:
        if abs(sample) <= 0.105:
            demodulatedData.append(0)
        else:
            demodulatedData.append(1)

    demodulatedData = np.asarray(demodulatedData)

    median = medfilt(demodulatedData, kernel_size=windowSize)
    deviation = np.abs(demodulatedData - median)
    threshold = 3 * np.median(deviation)

    smoothed_signal = np.where(deviation > threshold, median, demodulatedData)
    
    return smoothed_signal

def printWelcomeMessage():
    """
    This function prints the welcome message.
    """
    print("\n\n\n")
    print("\033[91mThis program generates a digital signal, modulates it onto a carrier wave, adds noise to it, and then demodulates it.\033[0m")
    print("\033[94mAfter that, the digital signal, carrier wave, the noise, the modulated signal, and the demodulated signal are shown using matplotlib.\033[0m")
    print("\n\n\n")

if __name__ == "__main__":
    printWelcomeMessage()

    t, square = generateSignal()
    carrier_wave, modulatedSignal = modulateSignal(t, square)
    noise, modulatedSignal = addNoise(modulatedSignal)
    demodulatedSignal = demodulateSignal(modulatedSignal)

    fig, axes = plt.subplots(nrows = 5, ncols = 1, figsize = (10, 8), num = "On Off Keying")
    axes[0].plot(t, square, color = "blue")
    axes[0].set_title("Original Data", color = "blue")
    axes[1].plot(t, carrier_wave, color = "green")
    axes[1].set_title("Carrier Wave", color = "green")
    axes[2].plot(t, noise, color = "red")
    axes[2].set_title("Noise", color = "red")
    axes[3].plot(t, modulatedSignal, color = "orange")
    axes[3].set_title("Modulated Signal", color = "orange")
    axes[4].plot(t, demodulatedSignal, color = "purple")
    axes[4].set_title("Demodulated Signal", color = "purple")

    for ax in axes.flat:
        ax.set_xlabel("Time(s)")
        ax.set_ylabel("Amplitude(V)")

    plt.tight_layout()
    plt.show()