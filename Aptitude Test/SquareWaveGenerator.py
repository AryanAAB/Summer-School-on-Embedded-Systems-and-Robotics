"""
SquareWaveGenerator.py

This program generates a square wave signal with user-defined
parameters such as amplitude, frequency, and sampling rate.

Usage:
- Create a custom square wave.
- Save the data in a csv file.

Dependencies:
- numpy
- matplotlib
- csv

@author: Aryan Bansal
@date: 25th April 2024
@version: 1.0
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

class NotPositiveError(Exception):
    """
    Custom error class raised when the inputed data is not positive.
    """
    def __init__(self, message="Number is not positive."):
        self.message = message

def generateSquareWave(amplitude: float, frequency: float, sampling_rate: float, duration=1.0):
    """
    Generates a square wave based on the given amplitude, frequency, sampling rate, and duration.
    
    Parameters:
    amplitude (float): The amplitude of the square wave.
    frequency (float): The frequency of the square wave.
    sampling_rate (float): The sampling rate of the square wave.
    duration (float, optional): The duration of the square wave in seconds. Defaults to 1.0.
    
    Returns:
    tuple: A tuple containing the time array and the square wave array.
    """
    # Calculate the time array
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    
    # Initialize square wave array
    square_wave = np.zeros_like(t)
    
    # Generate square wave by summing sine waves
    for n in range(1, 10000):  # We sum up to the 10,000th harmonic for a good approximation
        square_wave += (4 / (2*n - 1) / np.pi) * np.sin(2 * np.pi * (2*n - 1) * frequency * t)
    
    square_wave *= amplitude  # Normalize amplitude
    
    return t, square_wave

def getNumber(message: str, isPositive=False):
    """
    Returns a number provided by the user.
    
    Parameters:
    message (str): The message to be displayed when prompting the user for input.
    isPositive (bool, optional): If True, only positive numbers are accepted. Defaults to False.
    
    Returns:
    float: The number provided by the user.
    """
    while True:
        try:
            x = input(message)
            x = float(x)

            if not (isPositive and x <= 0):
                return x
            else:
                raise NotPositiveError()
        except ValueError:
            print("Please enter a number.")
        except NotPositiveError:
            print("Please enter a positive number.")

def formatValues(values):
    """
    Formats values with appropriate units based on their magnitudes.
    
    Parameters:
    values (list of float): The values to be formatted.
    
    Returns:
    tuple: A tuple containing the formatted values and the appropriate unit.
    """
    magnitude = max(abs(value) for value in values)
    units = ['T', 'G', 'M', 'k', '', 'm', 'μ', 'n', 'p']
    threshold_values = [1e12, 1e9, 1e6, 1e3, 1, 1e-3, 1e-6, 1e-9, 1e-12]
    for i, threshold in enumerate(threshold_values):
        if magnitude >= threshold:
            return (['{:.3f}'.format(value / threshold) for value in values], units[i])
    return (['{:.3f}'.format(value) for value in values], "")


def printWelcomeMessage():
    """
    This function prints the welcome message.
    """
    print("\n\n\n")
    print("\033[91mThis program generates a square wave on matplotlib based on the amplitude, frequency, and sampling rate entered by you.\033[0m")
    print("\033[94mMake sure that the frequency and the sampling rate are positive numbers and the amplitude is a number.\033[0m")
    print("\033[92mMoreover, make sure that you select enough sampling points based on your frequency to generate a proper square wave.\033[0m")
    print("\033[93mIn the end, the data points of the square wave would be saved in the csv file called \"square_wave_data.csv.\"\033[0m")
    print("\n\n\n")

if(__name__ == "__main__"):
    printWelcomeMessage()

    # User-defined parameters
    amplitude = getNumber("Please enter the amplitude of the square wave in V (should be a number): ", False)
    frequency = getNumber("Please enter the frequency of the square wave in Hz (should be a positive number): ", True)
    sampling_rate = getNumber("Please enter the sampling rate of the sqaure wave in Hz (should be a positive number): ", True)

    # Generate the square wave
    t, square_wave = generateSquareWave(amplitude, frequency, sampling_rate)

    # Plot the square wave
    plt.figure("Square Wave Generator")
    plt.plot(t, square_wave)
    plt.title('Square Wave (Sampling Rate: {} Hz)'.format(sampling_rate))
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (V)')
    plt.grid(True)

    plt.show()

    # Format the time and amplitude values
    formatted_time, prefix_time = formatValues(t)
    formatted_amplitude, prefix_amplitude = formatValues(square_wave)

    # Save the formatted data to a CSV file
    try:
        formatted_data = list(zip(formatted_time, formatted_amplitude))
        with open('square_wave_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Time(' + prefix_time + 's)', 'Amplitude(' + prefix_amplitude + 'V)'])
            writer.writerows(formatted_data)
    except Exception:
        print("\033[91mCannot write to file.\033[0m")
    
    print("\n\n\n")