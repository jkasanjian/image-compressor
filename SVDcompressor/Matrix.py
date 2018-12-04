"""
Matrix.py
Author: Joshua Kasanjian
Description: An implementation of the Matrix data type, with
overloaded operators and other functions for various calculations.  
"""

import numpy, math
from Vec import Vec

"""
Matrix class
Attributes:
    Rowsp (List): List of lists representing the rows of the matrix
    Colsp (List): List of lists representing the columns of the matrix
"""
class Matrix:
    
    def __init__(self, Rows = []):
        """
        Constructor to initialize Matrix
        Parameters:
            Rows (List): List of lists for the rows of Matrix (defaults to empty list)
        """
        self.Rowsp = Rows
        self.Colsp = []
        
        numrows = len(self.Rowsp[0])
        
        for i in range(numrows):
            temp = []
            c = 0
            while(c < len(self.Rowsp)):
                temp.append(self.Rowsp[c][i])
                c = c + 1
    
            self.Colsp.append(temp)    
        return

                        
    def __str__(self):
        """Converts Matrix to string for print statemets """ 
        m = ""
        for i in range(len(self.Rowsp)):
            for j in range(len(self.Rowsp[0])):
                m += str(self.Rowsp[i][j]) + '\t'
            m += "\n"
        return m
    
    #getters
    def getCol(self, j):
        j = j-1
        return self.Colsp[j]

    def getRow(self, i):
        i = i-1
        return self.Rowsp[i]
    
    def getEntry(self, i, j):
        i = i-1
        j = j-1
        return self.Rowsp[i][j]
 
    def getColSpace(self):
        return self.Colsp
    
    def getRowSpace(self):
        return self.Rowsp

    #returns a diagonal of the matrix
    def getdiag(self, k):
        diag = []
        
        if(k == 0):
            r = 0
            c = 0
        elif(k > 0):
            r = 0
            c = k
        elif(k < 0):
            r = abs(k)
            c = 0
        
        while(len(diag) < (len(self.Rowsp[0]) - abs(k))):
            diag.append(self.Rowsp[r][c])
            r = r + 1
            c = c + 1

        return diag

    #sets column of matrix
    def setCol(self, j, u):
        if(len(u) == len(self.Colsp[0])):
            j = j-1
            self.Colsp[j] = u
            for n in range(len(self.Rowsp)):
                self.Rowsp[n][j] = u[n]
        else:
            raise ValueError("Incompatible column length.")

    #sets row of matrix
    def setRow(self,i, v):
        if(len(v) == len(self.Rowsp[0])):
            i = i - 1
            self.Rowsp[i] = v            
            for n in range(len(self.Colsp)):
                self.Colsp[n][i] = v[n]
        else:
            print("ERROR: Incompatible row length.")
            #raise ValueError("Incompatible row length.")
    
    def setEntry(self,i, j, a):
        i = i-1
        j = j-1
        
        self.Rowsp[i][j] = a
        self.Colsp[j][i] = a
    
    #overloads addition operator
    def __add__(self, other):
        if(len(self.Rowsp) == len(other.Rowsp) and len(self.Colsp) == len(other.Colsp)):
            newRowsp = []
            for i in range(len(self.Rowsp)):
                newRow = []
                for j in range(len(self.Rowsp[0])):
                    newRow.append(self.Rowsp[i][j] + other.Rowsp[i][j])
                newRowsp.append(newRow)
            result = Matrix(newRowsp)
            return result
        else:
            print("ERROR: Dimension mismatch.")
    
    #overloads subtraction operator
    def __sub__(self, other):
        return self + (-1.0 * other)
        
    #overloads multiplication operator
    #accommodates if Matrix is being multiplied by a number, a Vector, or another Matrix
    def __mul__(self, other):
        if type(other) == float:
            newRowsp = []
            for i in range(len(self.Rowsp)):
                newRow = []
                for j in range(len(self.Rowsp[0])):
                    newRow.append(self.Rowsp[i][j] * other)
                newRowsp.append(newRow)
            result = Matrix(newRowsp)
            return result
            
        elif type(other) == Matrix:
            if(len(self.Colsp) == len(other.Rowsp)):
                calc = numpy.matmul(self.Rowsp, other.Rowsp)
                return Matrix(calc)
                newRowsp = []
                
                for i in range(len(self.Rowsp)):
                    oneRow = []
                    for j in range(len(other.Rowsp[0])):
                        entry = 0
                        for k in range(len(other.Rowsp)):
                            entry+= self.Rowsp[i][k] * other.Rowsp[k][j]
                        oneRow.append(entry)
                    newRowsp.append(oneRow)
                return Matrix(newRowsp)
            else:
                print("ERROR: Dimension mismatch. ")
                return
            
        elif type(other) == Vec:
            a = other.vec
            entry = []
            newRowsp = []
            for i in range(len(a)):
                entry = []
                entry.append(a[i])
                newRowsp.append(entry)
            vect = Matrix(newRowsp) #creates matrix from the vector
            return self * vect #multiplies using matrix-matrix multiplication operator
        else:
            print("ERROR: Unsupported Type.")
        return
    
    
    def __rmul__(self, other):  #if left side is not a matrix
        if type(other) == float:
            return self * other
        else:
            print("ERROR: Unsupported Type.")
            
    #solves a linear equation of the form Ax = b where A is a matrix and b is a vector
    def solve(A,b):
        #checking if upper diagonal
        isValid = True
        for i in range(len(A.Rowsp)):
            d = A.getdiag(-1 * (i+1))
            for e in d:
                if e != 0:
                    isValid = False
                    
        if isValid:
            x = []
            n = len(A.Rowsp[0])
            for z in range(n):
                x.append(0)
            b = b.Rowsp  
            for i in reversed(range(n)):
                add = []
                for k in range(n):
                    add.append(A.Rowsp[i][k] * x[k])
                x[i] = (b[i][0] - sum(add)) / A.Rowsp[i][i]
            return Vec(x)
        
        else:
            print("Unsupported Matrix Type")

     
    def dim(self):
        """returns the dimensions of this Matrix object
        OUTPUT: tuple (m, n) where m is the number of rows 
        of this matrix and n is the number of columns of this matrix
        """
        m = len(self.Rowsp)
        n = len(self.Colsp)
        return (m, n)
            
        
    def swapRows(self, i, j):
        """swaps the i-th and j-th rows of this matrix
        INPUT: i, j - integer index of the rows to swap
        OUTPUT: None
        """
        temp = self.Rowsp[i-1]
        self.setRow(i, self.Rowsp[j-1])
        self.setRow(j, temp)
        
    
    def swapCols(self, i, j):
        """swaps the i-th and j-th columns of this matrix
        INPUT: i, j - integer index of the columns to swap
        OUTPUT: None
        """
        temp = self.Colsp[i-1]
        self.setCol(i, self.Colsp[j-1])
        self.setCol(j, temp)
        
    
    def rank(self):
        """returns the rank form of matrix A
        INPUT: A - n X m matrix
        OUTPUT: rank of A as an integer
        """
        rank = 0
        A = MatrixSolvers.RREF(self)
        for row in A.Rowsp:
            if abs(Vec(row)) != 0.0:
                rank += 1
        return rank

    #transposes Matrix
    def transpose(self):
        cols = self.Colsp
        return Matrix(cols)

    #returns a lamba Matrix
    def getLambdaMatrix(self, n):
        A = self
        for i in range(len(self.Rowsp)):
            A.Rowsp[i][i] = self.Rowsp[i][i] - n
        return A
