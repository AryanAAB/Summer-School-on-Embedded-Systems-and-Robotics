# Aptitude Test

## Square Wave Generator

### Description
SquareWaveGenerator.py generates a square wave with user-defined amplitude, frequency, and samples per second. These parameters dictate the characteristics of the square wave to be generated. Once the user provides these values, the code uses the “NumPy” library to create a square wave signal using the Fourier Series. It computes the time value corresponding to each sample point based on the specified samples per second. As a result, it is important the sampling frequency is large enough to capture the essence of the square wave. Then, using these time values, it generates the square wave and plots it using “Matplotlib”. Finally, the time and amplitude data are stored in “square_wave_data.csv” file using the “CSV” module. This way, users can visualize and utilize the generated square waves according to their requirements.

### Snippets of Important Sections
The below code generates a square wave given the amplitude, frequency, and sampling rate with a default duration of 1 second. It uses Fourier Series to generate the square wave. 
```python
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
```
The below code gets the user data, generates the square wave, and writes to the csv file.
```python
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
```
### Running the Code
python3 SquareWaveGenerator.py

## Analog to Digital Converter

### Description
ADC.py mimics the analog to digital converter calculator by taking in the number of bits in ADC, the analog voltage input to ADC, and the reference voltage to ADC and outputting the numeric digital output and binary digital output. In other words, it takes a voltage or current input and converts it into a digital representation that can be processed by digital systems like microcontrollers, computers, or digital signal processors. 

### Snippets of Important Sections
The below code gets the user data
```python
def getInteger(message: str):
    """
    Prompts the user to enter an integer and keeps asking until a valid integer is provided.
    
    Parameters:
    message (str): The message to display when prompting the user for input.
    
    Returns:
    int: The valid integer entered by the user.
    """
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Please enter a valid integer")

def getFloat(message: str):
    """
    Prompts the user to enter a float and keeps asking until a valid float is provided.
    
    Parameters:
    message (str): The message to display when prompting the user for input.
    
    Returns:
    float: The valid float entered by the user.
    """
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Please enter a valid integer")
```
The below code uses the number of bits, analog voltage, and the reference voltage to find the numeric and binary digital outputs.
```python
if __name__ == "__main__":

    printWelcomeMessage()
    bits = getInteger("Please enter the number of bits in ADC: ")
    analogVoltage = getFloat("Please enter the Analog Voltage input to ADC in Volts: ")
    referenceVoltage = getFloat("Please enter the Reference Voltage to ADC in Volts: ")

    ans = int((1 << bits) * analogVoltage / referenceVoltage)

    print("\n\033[93mNumeric Digital Output: ", ans, "\033[0m", sep = "")
    print("\033[95mBinary Digital Output: ", bin(ans)[2:], "\033[0m", sep = "")
    print("\n\n\n")
```

### Running the Code
python3 ADC.py

### Python Package to Facilitate Basic Mathematical Operations

### Description
The package I created was “aryan-basic-math-operations” using PyPI. This package provides basic functionality for operations such as addition, subtraction, multiplication, division, power, integer division, left shift, and right shift for two numbers. The url to the package is [https://pypi.org/project/aryan-basic-math-operations/](https://pypi.org/project/aryan-basic-math-operations/).  

### Installation
To install the package run the following command: 
  * pip install aryan-basic-math-operations
To use the package run the following command:
  *	from basic_math_operations import *
  *	After that, you can call the different methods available such as add, subtract, multiply, and others as shown below. 

### Sample Use of the program
```python
from basic_math_operations import *

if __name__ == "__main__":
    result_add = add(5, 3)
    result_subtract = subtract(5, 3)
    result_multiply = multiply(5, 3)
    result_divide = divide(5, 3)
    result_pow = pow(5, 3)
    result_int_divide = intDivide(5, 3)
    result_left_shift = leftShift(5, 3)
    result_right_shift = rightShift(5, 3)

    print(result_add)           # Output: 8
    print(result_subtract)      # Output: 2
    print(result_multiply)      # Output: 15
    print(result_divide)        # Output: 1.67
    print(result_pow)           # Output: 125
    print(result_int_divide)    # Output: 1
    print(result_left_shift)    # Output: 40
    print(result_right_shift)   # Output: 0
```

### Running the Code
python3 Math.py

### Current Flowing through a Resistor

### Introduction to Electric Circuits
In an electric circuit, an energy source such as a battery and an energy-consuming device such as a resistor are connected via conducting wires which allows the flow of electric charges and thus the transfer for energy. Due to a chemical reaction in the battery, electrons are transferred from one terminal (leaving it positively charged) to another terminal (leaving it negatively charged). Inside a wire, the battery creates an electric field, due to a potential difference V between the positive terminal and the negative terminal, which exerts a force on the free electrons. This flow of charge is called electric current (I). In modern day scenarios, we often use conventional current, which represents the hypothetical flow of positive charges that has the same effect as the flow of negative charges. As a result, the conventional current always points in the direction from higher potential to lower potential while actual electron flow goes from lower to higher potential. 

### Ohm's Law
The ratio of voltage V applied across a substance or device to the current through the material is called resistance. For many materials, this ratio remains constant for a wide range of voltages and currents. Since the relation R = V/I was discovered by Georg Simon Ohm, it is known as Ohm’s Law and the SI unit of resistance is V/A or Ohm (Ω). 

### Factors Affecting Resistance
**Physical Dimensions:** The resistance (R) of a resistor is directly proportional to its length (𝐿) and inversely proportional to its cross-sectional area (𝐴). The relationship is given by: R=ρ L/A

**Material Properties:** The resistivity (ρ) of the material from which the resistor is made significantly influences its resistance (R). Different materials have different resistivities, affecting their suitability for various applications.

**Temperature:** Most materials exhibit a change in resistance (ΔR) with change in temperature (ΔT). The relationship is described by the temperature coefficient of resistance (α), where: ΔR=R_0 αΔT

### Material's that Behave Differently
While most materials follow Ohm’s Law and the above conditions under normal conditions, there are certain materials and scenarios where the relationship may not hold true. For example,
  1.	Semiconductors or Light-Emitting Diodes(LEDs): Unlike metals, semiconductors such as silicion and germainum do not strictly follow Ohm’s Law. Their resistance can vary significantly with chnages in temperature, doping level, and applied voltage. Some examples of semiconductor devices are LED’s, diodes, and transistors.
  2.	Superconductors: Superconductors exhibit zero electrical resistance below a critical temperature. When cooled below this critical temperature, superconductors condut electricity without any loss of energy. In this state, the relationship between voltage and current is not described by Ohm’s Law because there is no resistance to impede the flow of current.
  3.	Non-Ohmic Conductors: Some materials exhibit non-Ohmic behavior, meaning their resistance changes with changes in voltage or current. For instance, certain electrolytes, semiconductors operating near breakdown voltage, and materials undergoing phase transitions. In these cases, the resistance may vary nonlinearly with voltage or current.

### Experiement: Investigation of Ohm’s Law with Various Resistors
**Objective:** The objective of this experiment is to investigate Ohm’s Law by measuring the relationship between current (I) and resistance (R) when connected to a fixed voltage source of 5V. 

**Hypothesis:** Increasing the resistance of the resistor will result in a decrease in the current flowing through it when voltage is kept constant, because the higher resistance values would impede the flow of current. 

**Materials:**
  *	Various resistors of different resistance values
  *	DC power supply suppy such as a battery
  *	Connecting Wires
  *	Multimeter to measure voltage, current, and resistance
  *	Breadboard

**Procedure:**
  1.	Connect the DC power supply to the breadboard.
  2.	Chose a resistor and measure its resistance using a Ohmeter or Multimeter.
  3.	Connect one terminal of the resistor to the positve terminal of the power supply and anoother terminal to the negative terminal of the power supply.
  4.	Ensure all connections are secure and there are no short circuits.
  5.	Record the voltage and the current through each resistor.
  6.	Repeat for the other resistance values.
  7.	Plot the graph of current (I) versus resistance (R) for each resistor.

**Precautions:**
  1.	Handle the power supply and the electrical connections with care to avoid electric shock.
  2.	Ensure the connections are secure to prevent short circuits and overheating of components.
  3.	Do not exceed the maximum rated voltage and current of the resistors and other components. 

**Analysis:**
analysis of the chart depicting the relationship between current (I) and the reciprocal of resistance (1/R) reveals a linear trend, as evidenced by the straight line of best fit. This linear relationship supports Ohm's Law, which states that the current flowing through a resistor is directly proportional to the inverse of its resistance when subjected to a constant voltage. The slope of the line represents the voltage connected across the resistor. Additionally, the y-intercept of the line provides insight into the current that would flow through the circuit if the resistance became very high. In practical terms, this intercept means that as resistance increases, the current through the resistor decreases which is in accordance to Ohm’s Law.

**Conclusion:**
Through the experiment, it is evident that the current through a resistor, denoted as I(R), is inversely proportional to the resistor value, R, when the resistor is connected across a voltage source, V, in a practical setting. By measuring the voltage and current across different resistors connected to a fixed 9 V battery, we observed a consistent linear trend between current and the reciprocal of resistance as predicted by Ohm’s Law.

## On-Off Keying Modulation and Demodulation

### Importance of Modulating a Signal with a Carrier in Communication Systems
Modulation is a process by which data is converted into waves by using a carrier signal, whereas demodulation is a process by which the received waves are converted back into useful data. A carrier signal does not contain any information but posesses a unique phase, frequency, or amplitude upon which the data is superimposed. There are three types of modulation: frequency modulation, phase modulation, and amplitude modulation. In frequency modulation, the frequency of the carrier wave is varied; in phase modulation, the phase of the carrier signal is modified; and in amplitude modulation, the amplitude of the carrier signal represents the data. An example of amplitude modulation is On-Off Keying Modulation in which if the transmitter goes to IDLE state, then the transmission is logic 0; otherwise, the transmission is logic 1. 
Modulation is important because of the following reasons:
  * **Efficient Data Transmission:** Transmitting a signal over a link often results in significant signal degradation due to attentuation, distortion, and intereference. As a result, the carrier signals typically have a much higher frequency than the information signal which allows the carrier signal to travel longer distances with less attenuation as compared to the original signal.
  *	**Wireless Communication:** Modulating a signal allows us to tranmit signals over long distances wirelesly. Earlier, wires were drawn across large parts of the continent, but it was not possible to make them available everywhere. Modulating allows us to provide services to remote locations quickly and also saves the cost of drawing a dedicated wire to that place.
  *	 **Reduction in the Height of the Antenna:** For transmitting data, the height of the antenna is usually proportional to the wavelength of the signal. One cannot install an antenna for low frequency signals(signals with larger wavelengths) because the height would be too big. As a result, modulating these signals on high frequency signals allows one to reduce the size of the antenna.
  *	**Multiplexing is Possible:** Modulation allows two or more signals to be transmitted at the same over the same link through the process of modulation. As a result, signals of the same frequency range can be sent without getting them mixed with each other.

### Description
OOK (On-Off Keying) modulation is a type of digital modulation where the presence or absence of a carrier wave represents digital data. In OOK modulation, the carrier signal is turned on and off to encode binary data. When the carrier is on, it represents one binary state (often '1'), and when it's off, it represents the other binary state (often '0'). 
OnOffKeying.py generates a digital signal and modulates it onto a carrier wave using On-Off Keying Modulation with the help of “numpy” and “scipy.signal”. Next, some noise is added to the modulated wave. After transmission, the modulated signal is demodulated at the receiver by detecting the presence or absense of the carrier wave during each cycle. This allows the program to reconstruct the digital signal. Finally, the original signal, carrier wave, noise, modulated signal, and the demodulated signal are shown using “Matplotlib”.

### Snippets of Important Sections
The below code generates the original binary data signal.
```python
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
```
The below code modulates the signal onto a carrier wave and then adds Gaussian noise to the modulated signal.
```python
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
```
The below code demodulates the signal.
```python
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
```
### Running the program
python3 OnOffKeying.py
