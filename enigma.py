import string

from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard

alphabet = string.ascii_uppercase

class Enigma:

    def __init__(self):
        self.rotors = []
        self.plugboards = []
        self.setup()

    def setup(self):

        # Initialise reflector
        reflectorWiring = "EJMZALYXVBWFCRQUONTSPIHGKD"
        reflectorInstance = Reflector(reflectorWiring)
        self.reflector = reflectorInstance

        # Dictionary of rotors
        rotorSettings =["EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q',
                         "AJDKSIRUXBLHWTMCQGZNPYFVOE", 'E',
                         "BDFHJLCPRTXVZNYEIWGAKMUSQO", 'V'
                        ]
        
        # Add rotors
        for wiring, notch in rotorSettings:
            self.addRotorPlugboard(wiring, notch)

    def addRotorPlugboard(self, wiring, notch)
        swap = []

        # Set up pairs
        for i in range(26):
            swap.append((alphabet[i], wiring[i]))

        # Initialise plugboard 
        plugboardInstance = Plugboard(swap)
        self.plugboards.append(plugboardInstance)

        # Initialise rotor
        rotorInstance = Rotor(wiring, notch)
        self.rotors.append(rotorInstance)
            

