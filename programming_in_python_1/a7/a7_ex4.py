from a7_ex2 import Distance
    
class Manhattan(Distance):
    def __init__(self, x, vect1:list, vect2:list):
        super().__init__(x)
        self.vect1 = list(vect1)
        self.vect2 = list(vect2)
    def to_string(self):
        return f"{super().to_string()}, vector_1={self.vect1}, vector_2={self.vect2}"
    def dist(self):
        manh_dist = 0
        for i in range(len(self.vect1)):
            manh_dist += abs(self.vect1[i] - self.vect2[i]) 
        manh_dist = round(float(manh_dist), 4)
        return manh_dist
    

