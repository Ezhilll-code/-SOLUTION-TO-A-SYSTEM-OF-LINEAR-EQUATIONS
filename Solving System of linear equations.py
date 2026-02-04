#Program to find the solution for the given linear equations.
#Developed by: Ezhilan H
#RegisterNumber: 212225240040

import numpy as np

MatrixA = np.array([[1,-3],[3,1]])
MatrixB = np.array([0,10])

res = np.linalg.solve(MatrixA,MatrixB)

print(res)
