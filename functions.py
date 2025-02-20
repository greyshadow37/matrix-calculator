'''Import Statements'''
import numpy as np
from scipy.linalg import lu 
from scipy.linalg import null_space
from scipy.linalg import LinAlgError as LAerror


'''Functions to check for various conditions'''

# Function to compare whether the dimensions of two matrices are equal
def matrix_dim(arr1, arr2):
    return np.shape(arr1) == np.shape(arr2)


'''Functions for different Operations and Transformations'''

# Function to add, subtract or multiply two matrices
def matrix_arithmetic(arr1, arr2, oper):
    arr1 = np.array(arr1, dtype=float)
    arr2 = np.array(arr2, dtype=float)

    if oper == "Multiplication":
        if arr1.shape[1] == arr2.shape[0]:  
            return np.matmul(arr1, arr2).tolist()
        else:
            return "Error: Incompatible dimensions for multiplication"

    elif matrix_dim(arr1, arr2):
        if oper == "Addition":
            return np.add(arr1, arr2).tolist()
        elif oper == "Subtraction":
            return np.subtract(arr1, arr2).tolist()
        else:
            return "Error: Invalid operation"
    else:
        return "Error: Matrices have different dimensions"


# Function for transpose
def transpose(arr):
    arr = np.array(arr, dtype = float)
    try:
        transpose = np.transpose(arr)
        return transpose.tolist()
    except np.linalg.LinAlgError as e:
        return f"Error: {e}"

# Function to calculate inverse
def inverse(arr):
    arr = np.array(arr, dtype=float)
    try:
        inverse = np.linalg.inv(arr)
        return inverse.tolist()
    except np.linalg.LinAlgError as e:
        return f"Error: {e}"


# Function to calculate determinant
def determinant(arr):
    arr = np.array(arr, dtype=float)
    try:
        return np.linalg.det(arr)
    except np.linalg.LinAlgError as e:
        return f"Error: {e}"


# Function to calculate rank of a matrix
def rank(arr):
    arr = np.array(arr, dtype=float)
    try:
        return np.linalg.matrix_rank(arr)
    except np.linalg.LinAlgError as e:
        return f"Error: {e}"


# Function to calculate null space of a matrix
def nullSpace(arr):
    arr = np.array(arr, dtype=float)
    try:
        null_value = null_space(arr)
        return null_value.tolist()
    except LAerror as e:
        return f"Error: {e}"    

# Function to calculate Eigenvalues
def eigen(arr):
    arr = np.array(arr, dtype=float)
    try:
       return np.linalg.eigvals(arr)
    except np.linalg.LinAlgError as e:
        return f"Error: {e}" 

# Function to calculate LU decomposition
def LU(arr):
    arr = np.array(arr, dtype=float)
    try:
        P, L, U = lu(arr)
        return P.tolist(), L.tolist(), U.tolist()
    except LAerror as e:
        return f"Error: {e}"

# Function to calculate Singular Value Decomposition
def SVD(arr):
    arr = np.array(arr, dtype=float)
    try:
        U, s, Vh = np.linalg.svd(arr)
        return U.tolist(), s.tolist(), Vh.tolist()
    except LAerror as e:
        return f"Error: {e}"

