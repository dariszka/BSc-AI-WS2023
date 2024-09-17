class Radian:
    def __init__(self, degree: float):
        self.degree = float(degree)
    def rad(self):
        self.rad = (self.degree * (3.14/180))
        self.rad = float(f'{self.rad:0.2f}') #this is just for formatting purposes, 
                                             #so that it looks like in the example we were given, 
                                             #otherwise we would get 1.5700000000000003

        return self.rad
    def print(self):
        print(f'The degree is {self.degree:0.2f} and the radian is {self.rad:0.2f}')
