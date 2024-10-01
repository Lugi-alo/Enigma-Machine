class Plugboard:
    
    def __init__(self, wiring):
        self.wiring = wiring

    def swap(self, letter):
        return self.wiring.get(letter, letter)
        
        

