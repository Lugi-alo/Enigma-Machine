class Plugboard:
    
    def __init__(self, wiring):
        self.wiring = {}
        for char in string.ascii_uppercase:
            self.wiring[char] = char

    def swap(self, letter):
        return self.wiring.get(letter, letter)
        
        

