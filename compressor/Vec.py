"""
Vec.py
Author: Joshua Kasanjian
Description: An implementation of the Vector data type, with overloaded
operators and other functions for various calculations.
"""


import math


class Vec:
    
    def __init__(self, contents = []):
        """
        Constructor to initialize Vec
        Attributes:
            contents (List): List with elements in vector (defaults to empty list)
        """
        self.vec = contents
        return
    
    def add(self, element, *positions): # this allows the user to enter as many elements
        # as desired, and the inputs get stored into a list called positions
        """
        adds the given element at the given positions
        INPUT:   element - the new element
                 positions - a list of integers
        """
        if len(positions) == 0:
            self.vec.append(element)
        else:
            k = 0
            for p in positions:
                self.vec.insert(p+k, element)
                k += 1
        return
    
    def remove(self, *positions):
        """
        removes the elements at the given positions
        INPUT: positions - list of integers
        """
        k = 0
        for p in positions:
            del self.vec[p - k]
            k += 1
            
    #overloaded addition operator for vector vector addition
    def __add__(self, other):
        if type(self) == Vec and type(other) == Vec:
            if len(self.vec) == len(other.vec):
                return Vec([self.vec[i] + other.vec[i] for i in range(len(self.vec))])
            else:
                print("ERROR: Incompatible vector lengths.")
                return Vec()
        return
    
    #overloaded multiplication operator
    #accounts for multiplying with vectors and numbers
    def __mul__(self, other):
        if type(self) == Vec and type(other) == Vec:
            if len(self.vec) == len(other.vec):
                return sum([self.vec[i] * other.vec[i] for i in range(len(self.vec))])
            else:
                print("ERROR: Incompatible vector lengths")
                return None
        elif type(self) == Vec and (type(other) == float or type(other) == int):
            return Vec([other * self.vec[i] for i in range(len(self.vec)) ])
        return
    
    #if left side is not a vector
    def __rmul__(self, other):
        if type(self) == Vec and (type(other) == float or type(other) == int):
            return Vec([other * self.vec[i] for i in range(len(self.vec)) ])
        return None

    #converts vector to string for print statements
    def __str__(self):
        return str(self.vec)
    
    def norm(v, p):
        """returns the p-norm of the vector v"""
        result = 0
        if p == 1:
            for u in v.vec:
                result = result + abs(u)
        elif p == 2:
            for u in v.vec:
                result = result + (u * u)
            result = math.sqrt(result)
             
        return  result

    #returns the absolute value of a vector
    def __abs__(self):
        sum = 0.0
        for i in range(len(self.vec)):
            sum += (self.vec[i] ** 2)
        return math.sqrt(sum) 
