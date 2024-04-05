from linear_algebra import vectors

if __name__ == "__main__":
    print("Vectors: ")
    s = vectors.Vector(1,2)
    print(s.get_vector())

    r = vectors.Vector(3,4)
    print(r.get_vector())
    
    calc = vectors.Calculator()
    print("Vector operations(add, multiply, multiply by scalar, subtract): ")
    print(calc.add_vectors(s, r))
    print(calc.multiply_vectors(s, r))
    print(calc.multiply_vector_by_scalar(s, 2))
    print(calc.subtract_vectors(s, r))
