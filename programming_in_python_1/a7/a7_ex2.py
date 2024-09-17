class Distance:
    def __init__(self, x):
        self.x = int(x)
    def to_string(self) -> str:
        return(f"{type(self).__name__}: the number of vectors ={self.x}")
    def dist(self) -> float:
        raise NotImplementedError
