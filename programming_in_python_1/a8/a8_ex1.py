import math

class Angle:
    def __init__(self, degree: float = None, radian : float = None):
        
        if degree is not None and radian is not None:
            if self.consistency(degree, radian) == False:
                raise ValueError("Degree and radian are not consistent.")
            self.degree = degree
            self.radian = radian
        elif degree is not None:
            self.degree = degree
            self.radian = Angle.deg_to_rad(degree)
        elif radian is not None:
            self.radian = radian
            self.degree = Angle.rad_to_deg(radian)
        else:
            raise ValueError("Either degree or radian must be specified.")

    def consistency(self, degree, radian):
        return math.isclose(degree, Angle.rad_to_deg(radian))
    
    def __eq__(self, other):
        if isinstance(other, Angle):
            if math.isclose(self.degree, other.degree) and math.isclose(self.radian, other.radian):
                return True
            else:
                return False
        else:
            return NotImplemented
        
    def __repr__(self):
        return f"Angle(degree={self.degree:0.3f}, radian={self.radian:0.3f})"
    
    def __str__(self):
        return f"{self.degree:0.2f} deg = {self.radian:0.2f} rad"

    def __add__(self, other):
        if isinstance(other, Angle):
            return Angle(self.degree + other.degree, self.radian + other.radian)
        else:
            return NotImplemented
        
    def __iadd__(self, other):
        if isinstance(other, Angle):
            self.degree += other.degree
            self.radian += other.radian
            if self.consistency(self.degree, self.radian) == False:
                raise ValueError("Degree and radian are not consistent.")
            return self
        else:
            return NotImplemented
 
    @staticmethod
    def deg_to_rad(degree):
        return degree * (math.pi / 180)

    @staticmethod
    def rad_to_deg(radian):
        return radian * (180 / math.pi)
    
    @staticmethod 
    def add_all(angle, *angles):
        degrees = angle.degree
        radians = angle.radian

        for a in angles:
            degrees += a.degree
            radians += a.radian

        return Angle(degrees, radians)
            

