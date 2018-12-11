import compressor.SVDCalculator as svdC

"""
Application.py
Author: Joshua Kasanjian
Description: Code to run application. Run main() to start.
"""


def main():
    """
    Main method where users enter the name of the black and white image
    file they wish to compress and k value of the approximation. The file
    must be in the same directory as this file. The function will generate
    an image for the rank-k approximation in the same directory, and tell
    the user the cumulative energy and error of the compressed image.
    """

    choice = ""
    while choice != "n":
        file = input("Enter file name (must be .png): ") #TODO: verify image type
        data = svdC.png2graymatrix(file)     # converts image to matrix
        rank = min(data.dim())     # gets rank of matrix
        print("Rank of image matrix:", rank)
        k = int(input("Enter k value (must be less than rank): "))
        while k > rank: 
            k = int(input("Please enter a valid number: "))
        print("Working...")
    
        result = svdC.SVD(data, k)   # returns rank k approximation and sigma values
        s = result[1]           # gets list of sigma values
        compressedData = result[0]      # image matrix after compression
        cE = svdC.cumulativeEnergy(s, k, rank) * 100  # gets cumulative energy of matrix
        error = svdC.calculateError(data, compressedData)    # calculates error between both matrices

        newFile = "compressed_" + file
        svdC.graymatrix2png(compressedData, newFile)   # creates compressed file
        print("\nRank-", k," approximation generated as ", newFile, sep='')           
        print("Cumulative energy of image: %.4f%%" % cE) 
        print("Error between image matrices: %.2f" % error)

        choice = input("\nWould you like to compress another image? (y/n): ")

main()