import string

alphabet = string.ascii_uppercase

class Plugboard:
    
    def __init__(self, swap=None):
        self.mapping = {}

        if swap is None:
            swap = []
            
        for letter in alphabet:
            self.mapping[letter] = letter
            
        for a, b in swap:
            self.mapping[a] = b
            self.mapping[b] = a

    def swap(self, letter):
        return self.mapping.get(letter, letter)
