# Aptitude Test

## Square Wave Generator

### Description
SquareWaveGenerator.py generates a square wave with user-defined amplitude, frequency, and samples per second. These parameters dictate the characteristics of the square wave to be generated. Once the user provides these values, the code uses the “NumPy” library to create a square wave signal using the Fourier Series. It computes the time value corresponding to each sample point based on the specified samples per second. As a result, it is important the sampling frequency is large enough to capture the essence of the square wave. Then, using these time values, it generates the square wave and plots it using “Matplotlib”. Finally, the time and amplitude data are stored in “square_wave_data.csv” file using the “CSV” module. This way, users can visualize and utilize the generated square waves according to their requirements.

### Running the Code
python3 SquareWaveGenerator.py

## Analog to Digital Converter

### Description
ADC.py mimics the analog to digital converter calculator by taking in the number of bits in ADC, the analog voltage input to ADC, and the reference voltage to ADC and outputting the numeric digital output and binary digital output. In other words, it takes a voltage or current input and converts it into a digital representation that can be processed by digital systems like microcontrollers, computers, or digital signal processors. 

### Running the Code
python3 ADC.py

### Python Package to Facilitate Basic Mathematical Operations

### Description
The package I created was “aryan-basic-math-operations” using PyPI. This package provides basic functionality for operations such as addition, subtraction, multiplication, division, power, integer division, left shift, and right shift for two numbers. The url to the package is [https://pypi.org/project/aryan-basic-math-operations/](https://pypi.org/project/aryan-basic-math-operations/).  

### Installation
To install the package run the following command: 
  • pip install aryan-basic-math-operations
To use the package run the following command:
  •	from basic_math_operations import *
  •	After that, you can call the different methods available such as add, subtract, multiply, and others as shown below. 

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
  •	Various resistors of different resistance values
  •	DC power supply suppy such as a battery
  •	Connecting Wires
  •	Multimeter to measure voltage, current, and resistance
  •	Breadboard
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
  • **Efficient Data Transmission:** Transmitting a signal over a link often results in significant signal degradation due to attentuation, distortion, and intereference. As a result, the carrier signals typically have a much higher frequency than the information signal which allows the carrier signal to travel longer distances with less attenuation as compared to the original signal.
  •	**Wireless Communication:** Modulating a signal allows us to tranmit signals over long distances wirelesly. Earlier, wires were drawn across large parts of the continent, but it was not possible to make them available everywhere. Modulating allows us to provide services to remote locations quickly and also saves the cost of drawing a dedicated wire to that place.
  •	 **Reduction in the Height of the Antenna:** For transmitting data, the height of the antenna is usually proportional to the wavelength of the signal. One cannot install an antenna for low frequency signals(signals with larger wavelengths) because the height would be too big. As a result, modulating these signals on high frequency signals allows one to reduce the size of the antenna.
  •	**Multiplexing is Possible:** Modulation allows two or more signals to be transmitted at the same over the same link through the process of modulation. As a result, signals of the same frequency range can be sent without getting them mixed with each other.

### Description
OOK (On-Off Keying) modulation is a type of digital modulation where the presence or absence of a carrier wave represents digital data. In OOK modulation, the carrier signal is turned on and off to encode binary data. When the carrier is on, it represents one binary state (often '1'), and when it's off, it represents the other binary state (often '0'). 
OnOffKeying.py generates a digital signal and modulates it onto a carrier wave using On-Off Keying Modulation with the help of “numpy” and “scipy.signal”. Next, some noise is added to the modulated wave. After transmission, the modulated signal is demodulated at the receiver by detecting the presence or absense of the carrier wave during each cycle. This allows the program to reconstruct the digital signal. Finally, the original signal, carrier wave, noise, modulated signal, and the demodulated signal are shown using “Matplotlib”.
