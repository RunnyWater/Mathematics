from math import sqrt
from linear_algebra.vector import Vector

class Calculator():

    def calculate_cosine(self, v1: Vector, v2: Vector) -> float:
        return (v1.x * v2.x + v1.y * v2.y) / (sqrt(v1.x**2 + v1.y**2) * sqrt(v2.x**2 + v2.y**2))
    
    def cosine_rule(self, v1: Vector, v2: Vector, cosine: float ) -> float:
        return v1.get_module()*v2.get_module()*cosine
        
