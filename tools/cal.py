

class Cal:
    # PyCryptodome: GCD
    # SageMath: GCD, gcd
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    
    def xgcd(self, a, b):
        if b == 0:
            # a = g = a * 1 + b * 0
            return a, 1, 0
        
        g, x1, y1 = self.xgcd(b, a % b)
        # g = x1 * b + y1 * (a % b)
        x = y1
        y = (g - a * x) // b
        assert a * x + b * y == g

        return g, x, y