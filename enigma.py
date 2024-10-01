from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard

class Enigma:

    def __init__(self):
        self.rotors = []
        self.setup()

    def setup(self):

        #initialise the first rotor
        rotorWiringI = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        rotorNotchI = 'Q'

        reflectorInstanceI = Reflector(rotorWiringI)
        plugboardInstanceI = Plugboard(rotorWiringI)

        rotorInstanceI = Rotor(rotorWiringI, rotorNotchI)
        self.rotors.append(rotorInstanceI)

        #initialise the second rotor
        rotorWiringII = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        rotorNotchII = 'E'
        
        reflectorInstanceII = Reflector(rotorWiringII)
        plugboardInstanceII = Plugboard(rotorWiringII)

        rotorInstanceII = Rotor(rotorWiringII, rotorNotchII)
        self.rotors.append(rotorInstanceII)
        
        #initialise the third rotor
        rotorWiringIII = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        rotorNotchIII = 'V'

        reflectorInstanceIII = Reflector(rotorWiringII)
        plugboardInstanceIII = Plugboard(rotorWiringIII)

        rotorInstanceIII = Rotor(rotorWiringIII, rotorNotchIII)
        self.rotors.append(rotorInstanceIII)

        return [rotorInstanceI, rotorInstanceII, rotorInstanceIII]

