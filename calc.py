import numpy as np

#function to check whether matrix is square matrix
def square_matrix(arr):
    return len(arr) == len(arr[0])

#function to compare whether the dimensions of two matrices are equal
def matrix_dim(arr1,arr2):
    return np.shape(arr1) == np.shape(arr2)

#operations on single matrix
def single_matrix(arr,oper):
    try:
        if oper == 1:
            return np.transpose(arr)
        if oper == 2:
            return np.linalg.det(arr)
        if oper == 3:
            return np.linalg.inv(arr)
        if oper == 4:
                return np.linalg.eigvals(arr)
        else:
            return "Error; Invalid operation"
    except np.linalg.LinAlgError as e:
        return f'error:{e}'

#operations on 2 matrices
def two_matrix(arr1,arr2,oper):
    if oper == 1:
        return np.add(arr1,arr2)
    if oper == 2:
        return np.subtract(arr1,arr2)
    else:
        return "Error; Invalid operation"
