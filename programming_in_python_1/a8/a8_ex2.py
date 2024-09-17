class Power:
    def __init__(self, exponent):
        if isinstance(exponent, (int, float)):
            self.exponent = exponent
        else:
            raise TypeError("The exponent must be a numerical value.")
    
    def __call__(self, x):
        if isinstance(x, (int, float)):
            return x**self.exponent
        else:
            raise TypeError("Input must be a numerical value.")
        
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Power(self.exponent + other)
        elif isinstance(other, Power):
            return Power(self.exponent + other.exponent)
        else:
            return NotImplemented
        
class Square(Power):
    def __init__(self):
        self.exponent = 2

