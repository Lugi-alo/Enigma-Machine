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

    def rotorRotation(self):
        
        # Rotate the first rotor
        rotate_next = self.rotors[0].rotate()

        # Handle double-stepping mechanism
        if rotate_next:
            if len(self.rotors) > 1:
                rotate_next = self.rotors[1].rotate()
                if rotate_next and len(self.rotors) > 2:
                    self.rotors[2].rotate()

    def encryption(self, letter):
        
        self.rotorRotation()
        print(f"\nEncrypting letter: {letter}")

        # Plugboard swap before rotors 
        letter = self.plugboard[0].swap(letter)
        print(f"After plugboard (Rotor 1): {letter}")

        # Forward pass through rotors
        for i, rotor in enumerate(self.rotors):
            letter = rotor.forward(letter)
            print(f"After rotor {i+1} forward: {letter}")

        # Reflector
        letter = self.reflector.reflect(letter)
        print("After reflector: " + letter )

        # Backward pass through rotors
        for i, rotor in enumerate(reversed(self.rotors)):
            letter = rotor.backward(letter)
            print("After rotor " + str(len(self.rotors)-i) + "backward: " + letter)

        # Use the plugboard corresponding to the last rotor after encrypting
        letter = self.plugboard[-1].swap(letter)
        print("Final encrypted letter:  " + letter)

        return letter

    def run(self):
        userInput = input("Enter your message: ").upper()
        encryptedOutput = ""

        for letter in userInput:
            if letter in alphabet:
                encryptedOutput = encryptedOutput + self.encryption(letter)
            else:
                encryptedOutput = encrpytedOutput + letter  

        print("\nEncrypted message: " + encryptedOutput)

# Main function
if __name__ == "__main__":
    enigmaMachine = Enigma()
    enigmaMachine.run()
