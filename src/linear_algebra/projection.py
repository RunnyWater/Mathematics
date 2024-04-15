from linear_algebra.vector import Vector
from linear_algebra import vectors

class Calculator:
    def __init__(self):
        self.calc = vectors.Calculator()

    def scalar_projection(self, v1: Vector, v2: Vector) -> float:
        # print(type(self.calc.multiply_vectors(v1, v2)))
        # print(type(v1.get_module()))
        return self.calc.multiply_vectors(v1, v2) / (v1.get_module())
    
    def vector_projection(self, v1: Vector, v2: Vector) -> Vector:
        scalar_projection = self.calc.multiply_vectors(v1, v2) / self.calc.multiply_vectors(v2, v2)
        return self.calc.multiply_vector_by_scalar(v2, scalar_projection)