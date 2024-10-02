class Rotor:

    def __init__(self, wiring, notch):
        self.wiring = wiring
        self.notch = notch
        self.position = 0

    def rotate(self):
        self.position = (self.position + 1) % 26
        return self.wiring[self.position] == self.notch

    def forward(self, letter):
        number = ord(letter) - ord('A')
        rearrangedNumber = (number + self.position) % 26
        return self.wiring[rearrangedNumber]
        
    def backward(self, letter):
        number = self.wiring.index(letter)
        rearrangedNumber = (number - self.position) % 26
        return chr(rearrangedNumber + ord('A'))
        
    

