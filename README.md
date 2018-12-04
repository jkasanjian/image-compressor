# svd-image-compressor

This Python 3 application can compress a black and white image using singular value decomposition.

The image is converted to a matrix with each element having the black intensity value of a pixel,
and operated on using self implemented Matrix and Vector classes. The program uses image.py to 
convert the black and white png file to pixel values.

The image generated is a rank-k approximation of the original image based on a user-entered k value. 
The higher the k-value, the more detailed the image, and the more space it takes up.
