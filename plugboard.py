import string

alphabet = string.ascii_uppercase

class Plugboard:
    
    def __init__(self, swaps=None):
        self.mapping = {}

        if swaps is None:
            swaps = []
            
        for letter in alphabet:
            self.mapping[letter] = letter
            
        for a, b in swaps:
            self.mapping[a] = b
            self.mapping[b] = a

    def swap(self, letter):
        return self.mapping.get(letter, letter)
