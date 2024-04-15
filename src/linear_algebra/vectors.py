import math 
from linear_algebra.vector import Vector

class Calculator:

    def add_vectors(self, v1: Vector, v2: Vector) -> Vector:
        return (v1.x + v2.x, v1.y + v2.y)
    
    def multiply_vectors(self, v1: Vector, v2: Vector) -> int:
        return v1.x * v2.x + v1.y * v2.y
    
    def multiply_vector_by_scalar(self, v1: Vector, scalar: int) -> Vector:
        return (v1.x * scalar, v1.y * scalar)
    
    def subtract_vectors(self, v1: Vector, v2: Vector) -> Vector:
        return (v1.x + v2.x*-1,  v1.y + v2.y*-1)
    
        

