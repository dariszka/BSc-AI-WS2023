from a7_ex3 import Minkowski
    
class Euclidean(Minkowski):
    def __init__(self, x, vect1:list, vect2:list):
        super().__init__(x, vect1, vect2)

    #I'm not defining the to_string again, since it defaults to the super class with this one's name,
    #which is what we want.

    #I'm not defining the distance again, since the square root of 2 is the same as the power of 1/2, 
    #like in the Minkowski distance class.

