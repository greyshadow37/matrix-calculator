# Import Statements
import numpy as np
from sympy import Matrix
from scipy.linalg import null_space
from scipy.linalg import LinAlgError as LAerror
import pandas as pd
import streamlit as st



# Function to compare whether the dimensions of two matrices are equal
def matrix_dim(arr1, arr2):
    return np.shape(arr1) == np.shape(arr2)
    

# Functions for different Operations and Transformations

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
    try:
        sympy_matrix = Matrix(arr)
        L, U, _ = sympy_matrix.LUdecomposition()  
        return L.tolist(), U.tolist()
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



st.header("Matrix Calculator")
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["Matrix Arithmetic","Transpose","Inverse","Determinant","Rank","Null Space","Eigenvalues","LU Decomposition","Singular Value Decomposition"]) 
cols = st.number_input("Number of Columns", min_value=1, value=3, step=1)
rows = st.number_input("Number of Rows", min_value=1, value=3, step=1)

default_matrix = pd.DataFrame(np.zeros((rows, cols)), columns=[f"Col {i+1}" for i in range(cols)])

with tab1:
    st.subheader("Matrix Arithmetic")
    matrix1 = st.data_editor(default_matrix, key="matrix1")
    matrix2 = st.data_editor(default_matrix, key="matrix2")
    operation = st.radio("Select Operation", ["Addition", "Subtraction", "Multiplication"])
    matrix1_values = matrix1.to_numpy()
    matrix2_values = matrix2.to_numpy()
    result = matrix_arithmetic(matrix1_values, matrix2_values, operation)
    st.subheader("Result:")
    if isinstance(result, str):
        st.error(result)
    else:
        st.dataframe(pd.DataFrame(result))

with tab2:
    st.subheader("Transpose")
    matrix = st.data_editor(default_matrix, key="matrix_transpose")
    matrix_values = matrix.to_numpy()
    result = transpose(matrix_values)
    st.subheader("Result:")
    if isinstance(result, str):
        st.error(result)
    else:
        st.dataframe(pd.DataFrame(result))

with tab3:
    st.subheader("Inverse")
    matrix = st.data_editor(default_matrix, key="matrix_inverse")
    matrix_values = matrix.to_numpy()
    result = inverse(matrix_values)
    st.subheader("Result:")
    if isinstance(result, str):
        st.error(result)
    else:
        st.dataframe(pd.DataFrame(result))

with tab4:
    st.subheader("Determinant")
    matrix = st.data_editor(default_matrix, key="matrix_determinant")
    result = determinant(matrix.to_numpy())
    st.subheader("Result:")
    st.write(result)

with tab5:
    st.subheader("Rank")
    matrix = st.data_editor(default_matrix, key="matrix_rank")
    result = rank(matrix.to_numpy())
    st.subheader("Result:")
    st.write(result)

with tab6:
    st.subheader("Null Space")
    matrix = st.data_editor(default_matrix, key="matrix_null_space")
    matrix_values = matrix.to_numpy()
    result = nullSpace(matrix_values)
    st.subheader("Result:")
    if isinstance(result, str):
        st.error(result)
    else:
        st.dataframe(pd.DataFrame(result))

with tab7:
    st.subheader("Eigenvalues")
    matrix = st.data_editor(default_matrix, key="matrix_eigenvalues")
    result = eigen(matrix.to_numpy())
    st.subheader("Result:")
    st.write(result)

with tab8:
    st.subheader("LU Decomposition")
    matrix = st.data_editor(default_matrix, key="matrix_lu")
    L, U = LU(matrix.to_numpy())
    st.subheader("L Matrix:")
    st.dataframe(pd.DataFrame(L))
    st.subheader("U Matrix:")
    st.dataframe(pd.DataFrame(U))

with tab9:
    st.subheader("Singular Value Decomposition (SVD)")
    matrix = st.data_editor(default_matrix, key="matrix_svd")
    U, s, Vh = SVD(matrix.to_numpy())
    st.subheader("U Matrix:")
    st.dataframe(pd.DataFrame(U))
    st.subheader("Singular Values:")
    st.write(s)
    st.subheader("Vh Matrix:")
    st.dataframe(pd.DataFrame(Vh))