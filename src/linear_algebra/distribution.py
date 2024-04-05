import math

class Distribution:
    def __init__(self, sigma, mu):
        self.sigma = sigma
        self.mu = mu

    def get_distribution(self):
        return (self.sigma, self.mu)
    

class Calculator:
    def calculate_equation (self, d: Distribution, x: float) -> float:
        return 1/d.sigma*math.sqrt(2*math.pi)* math.exp(-(x - d.mu)**2/(2*d.sigma**2))