# -SOLUTION-TO-A-SYSTEM-OF-LINEAR-EQUATIONS
## Aim:
To write a python program to find a solution to a system of linear equations.
## Equipment’s required:
1. 	Hardware – PCs
2. 	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
### Step 1: 
Import the numpy module to use the built-in functions for calculation
### Step 2: 
Prepare the lists from each linear equations and assign in np.array()
### Step 3: 
Using the np.linalg.solve(), we can find the solutions.
### Step 4: 
End the program
## Program:
```
#Program to find the solution for the given linear equations.
#Developed by: Ezhilan H
#RegisterNumber: 212225240040

import numpy as np

MatrixA = np.array([[1,-3],[3,1]])
MatrixB = np.array([0,10])

res = np.linalg.solve(MatrixA,MatrixB)

print(res)
```

## Output:
<img width="1302" height="585" alt="image" src="https://github.com/user-attachments/assets/afa79ba2-7abb-49a5-9692-9ca24ddaf2fa" />

## Result: 
Thus the solutions for the linear equations are successfully solved using python program

