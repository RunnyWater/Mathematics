from linear_algebra.vector import Vector
from linear_algebra import vectors
from linear_algebra import cosine
from linear_algebra import projection

if __name__ == "__main__":
    # print("Vectors: ")
    # s = Vector(1,2)
    # print(s.get_vector())

    # r = Vector(3,4)
    # print(r.get_vector())
    
    # calc = vectors.Calculator()
    # print("Vector operations(add, multiply, multiply by scalar, subtract): ")
    # print(calc.add_vectors(s, r))
    # print(calc.multiply_vectors(s, r))
    # print(calc.multiply_vector_by_scalar(s, 2))
    # print(calc.subtract_vectors(s, r))


    # print("Cosine: ")
    # v1 = Vector(3,2)
    # v2 = Vector(3,0)
    # calc = cosine.Calculator()
    # cosine = calc.calculate_cosine(v1, v2)
    # print(cosine)
    # print(calc.cosine_rule(v1, v2, cosine))


    print("Projection: ")
    v1 = Vector(3,2)
    v2 = Vector(3,0)
    calc = projection.Calculator()
    print(calc.scalar_projection(v1, v2))
    print(calc.vector_projection(v1, v2))