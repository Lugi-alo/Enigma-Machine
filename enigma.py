import string

from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard

alphabet = string.ascii_uppercase

class Enigma:
    
    def __init__(self):
        self.rotors = []
        self.plugboard = []
        self.reflector = None
        self.setup()

    def setup(self):
        
        # Initialise reflector
        reflectorWiring = "EJMZALYXVBWFCRQUONTSPIHGKD"
        self.reflector = Reflector(reflectorWiring)

        # Tuples of rotors
        rotorSettings = [
            ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q'),
            ("AJDKSIRUXBLHWTMCQGZNPYFVOE", 'E'),
            ("BDFHJLCPRTXVZNYEIWGAKMUSQO", 'V')
        ]

        # Add rotors 
        for wiring, notch in rotorSettings:
            rotorInstance = Rotor(wiring, notch)
            self.rotors.append(rotorInstance)

        # Initialise plugboard
        swaps = []
        for i in range(len(alphabet)):
            swaps.append((alphabet[i], wiring[i]))
        
        plugboardInstance = Plugboard(swaps)
        self.plugboard.append(plugboardInstance)


# Main function
if __name__ == "__main__":
    enigmaMachine = Enigma()
    enigmaMachine.run()
