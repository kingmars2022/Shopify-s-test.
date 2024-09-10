import sys

# Helper function to return Braille capital indicator symbol
def brailleCapitalIndicator():
    return '000001'

# Helper function to return Braille number indicator symbol
def brailleNumberIndicator():
    return '001111'

# Helper function to return Braille space symbol
def brailleSpace():
    return '000000'

# Mapping for letters and numbers to Braille
brailleAlphabet = {
    'a': '100000', 'b': '101000', 'c': '110000', 'd': '110100', 'e': '100100',
    'f': '111000', 'g': '111100', 'h': '101100', 'i': '011000', 'j': '011100',
    'k': '100010', 'l': '101010', 'm': '110010', 'n': '110110', 'o': '100110',
    'p': '111010', 'q': '111110', 'r': '101110', 's': '011010', 't': '011110',
    'u': '100011', 'v': '101011', 'w': '011101', 'x': '110011', 'y': '110111',
    'z': '100111'
}

brailleNumbers = {
    '0': '010110', '1': '100000', '2': '101000', '3': '110000', '4': '110100',
    '5': '100100', '6': '111000', '7': '111100', '8': '101100', '9': '011000'
}

def translator(inputString):
    """
    Function to translate input string to Braille.
    Handles letters, numbers, and spaces. Outputs Braille equivalent in 6-bit binary.
    """
    result = ""
    number_mode = False

    for char in inputString:
        if char.isalpha():  # Handle letters
            if char.isupper():
                result += brailleCapitalIndicator()  # Add capital indicator for uppercase letters
            result += brailleAlphabet[char.lower()]
        elif char.isdigit():  # Handle numbers
            if not number_mode:  # If number mode is not already active, add number indicator
                result += brailleNumberIndicator()
                number_mode = True
            result += brailleNumbers[char]
        elif char == " ":
            result += brailleSpace()  # Add Braille space
            number_mode = False  # Reset number mode after space

    return result

def main():
    """
    Main function to handle command-line input and perform the translation to Braille.
    """
    # Get the arguments from the command line
    input_args = sys.argv[1:]

    # Combine all input arguments into a single string
    inputString = " ".join(input_args)

    # Translate the input string to Braille
    translated_braille = translator(inputString)

    # Output the result to the terminal
    print(translated_braille)

if __name__ == "__main__":
    main()
