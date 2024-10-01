class Reflector:
    
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, letter):
        index = ord(letter) - ord('A')
        return self.wiring[index]

