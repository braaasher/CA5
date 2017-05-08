class Calculator(object):
 
    def __init__(self, a, b, x=0):
        self.a = a
        self.b = b
        self.x = x
    
    def add(self): 
        addition = map(lambda a: self.a + self.b, range(1-x))
        return addition 
        
    def subtract(self, x):
        subtraction = map(lambda a: self.a - self.b, range(1-x))
        return subtraction
    
    def multiply(self):
        multiplication = map(lambda a: self.a*self.b, range(10))
        return multiplication
    
    def divide(self):
        division = map(lambda a: self.a/self.b, range(10))
        return division
    
    def square(self):
        squares = map(lambda a: self.a*self.a, range(10))
        return squares

    def cube(self):
        cubes = map(lambda a: self.a*self.a*self.a, range(10))
        return cubes
    
    def expon(self):
        exp = map(lambda a: self.a*self.b, range(10))
        return exp
    
    def sqrt(self):
        squareroot = map(lambda a: self.a**(0.5), range(10))
        return self.a**(0.5)

    def pi(self):
        return_pi = map(lambda a: self.a*3.141592653589793238462643383279502884197169399375105820974944592307, range(10)) 
        return return_pi
        
    def factorial(self):
        self.b = 1
        while self.a >= 1:
            self.b = self.b * self.a
            self.a = self.a - 1
        return self.b
        
        