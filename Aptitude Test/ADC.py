"""
ADC.py

This program takes the number of bits in the ADC,
the analog voltage, and the reference voltage and
outputs the numeric and binary digital outputs. 

Usage:
- Create a custom square wave.
- Save the data in a csv file.

@author: Aryan Bansal
@date: 25th April 2024
@version: 1.0
"""

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

def printWelcomeMessage():
    """
    This function prints the welcome message.
    """

    print("\n\n\n")
    print("\033[91mThis program converts an analog input and provides a digita output based on the number of bits, analog voltage, and the reference voltage.\033[0m")
    print("\033[94mAnalog to Digital Converters(ADC's) are useful because microcontrollers can handle only digital signals.\033[0m")
    print("\033[92mFor example, if the microcontroller uses 0V as low and 5V as high, an ADC is required to convert any voltage signal in between to get a proper output.\033[0m")
    print("\n\n\n")

if __name__ == "__main__":

    printWelcomeMessage()
    bits = getInteger("Please enter the number of bits in ADC: ")
    analogVoltage = getFloat("Please enter the Analog Voltage input to ADC in Volts: ")
    referenceVoltage = getFloat("Please enter the Reference Voltage to ADC in Volts: ")

    ans = int((1 << bits) * analogVoltage / referenceVoltage)

    print("\n\033[93mNumeric Digital Output: ", ans, "\033[0m", sep = "")
    print("\033[95mBinary Digital Output: ", bin(ans)[2:], "\033[0m", sep = "")
    print("\n\n\n")