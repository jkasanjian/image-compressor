"""
SVDCalculator.py
Author: Joshua Kasanjian
Description: Uses Singular Value Decomposition to compress a black
and white image. 
"""

from compressor.image import file2image, isgray, image2file, color2gray
import numpy, math
from compressor.Matrix import Matrix


def png2graymatrix(filename):
    """
    Converts an image file to a Matrix object where each value is the
    grayscale value of a pixel.
    Uses functions from image.py by Philip N. Klein.
    """
    image_data = file2image(filename)
    if (isgray(image_data) == False):
        image_data = color2gray(image_data)
    return Matrix(image_data)


def graymatrix2png(img_matrix, path):
    """
    Converts a Matrix to a grayscale image file.
    Uses functions from image.py by Philip N. Klein.
    """
    data = img_matrix.getRowSpace()
    image2file(data, path)


def SVD(A,k):
    """
    Uses singular value decomposition to express image data as an approximation
    by calculating the eigenvalues and corresponding eigenvectors from the matrix
    of data. The rank of the approximation determines the number of eigenvalues and
    eigenvectos calculated to be used to reconstruct the image.

    Parameters:
        A (Matrix): data for image to be compressed.
        k (int): k value of approximation

    Returns:
        approx (Matrix): Matrix with rank-k approximation of original matrix
        s (List) : list of sigma values obtained from k
    """
    values = numpy.linalg.svd(A.Rowsp)
    U = values[0]
    V = values[2]
    
    AAT = A.transpose() * A
    vals = numpy.linalg.eigvals(AAT.Rowsp) #CALLED FUNCTION TO GET EIGENVALUES
    s = []                                 
    for v in vals:
        s.append(math.sqrt(abs(v)))  #converts eigenvalues to sigma values
    s.sort()
    s = s[::-1] #sigma values now in ascending order
    
    m=[[0 for x in range(k)] for y in range(k)] #forming sigma matrix from first k sigma values
    for i in range(0,k):
        m[i][i] = s[i] 
    
    newU = []
    l = len(U[0])
    for r in U:
        r2 = r[:-(l-k)]
        newU.append(r2) #removing columns so that there are k columns
        
    newV = []
    for a in range(k):
        newV.append(V[a]) #only taking first k rows
    
    U = Matrix(newU)
    S = Matrix(m)
    V = Matrix(newV)
    
    approx = U * S * V
    
    return approx, s
    
    
def cumulativeEnergy(s, k, r):
    """
    Calculates the cumulative energy of a rank-k approximation of an image.
    This represents the percentage of information the approximation retains
    from the original image.
    
    Parameters:
        s (List): list of sigma values
        k (int): k value of approximation
        r (int): rank of original matrix

    Returns:
        (float): cumulative energy of rank-k approximation
    """
    top = 0
    for i in range(k):
        top += (s[i] * s[i])
    
    bot = 0
    for j in range(r):
        bot += (s[j]*s[j])
    
    return top / bot 


def getKapprox(s, r, energy):
    """
    Calculates the approximate k value given the desired cumulative energy of the
    compressed image.

    Parameters:
        s (List): list of sigma values
        r (int): rank of matrix
        energy (float): desired cumulative energy

    Returns:
        k (int): rank of approximation 
    """
    bot = 0
    for i in range(r):
        bot += (s[i]*s[i])
    
    num = bot * energy
    top = 0
    k = 0
    while (top < num):
        top += (s[k]*s[k])
        k += 1
        
    return k


def calculateError(A, B):
    """
    Calculates the error between two Matrices

    Parameters:
        A, B (Matrix): matrices for calculation

    Returns:
        (float): error between A and B
    """
    errorMatrix = A - B
    total = 0
    for row in errorMatrix.Rowsp:
        for entry in row:
            total += (entry * entry)
    return math.sqrt(total)




