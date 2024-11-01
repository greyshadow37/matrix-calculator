'''Import Statements'''
import numpy as np
import gradio as gr
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

    print("Matrix 1 shape:", arr1.shape)  
    print("Matrix 2 shape:", arr2.shape)  

    if oper == "Multiplication":
        if arr1.shape[1] == arr2.shape[0]:  
            return np.matmul(arr1, arr2)
        else:
            return "Error: Incompatible dimensions for multiplication"
    elif matrix_dim(arr1, arr2):
        if oper == "Addition":
            return np.add(arr1, arr2)
        elif oper == "Subtraction":
            return np.subtract(arr1, arr2)
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
    arr = np.array(arr)
    try:
        inverse = np.linalg.inv(arr)
        return inverse.tolist()
    except np.linalg.LinAlgError as e:
        return f"Error: {e}"


# Function to calculate determinant
def determinant(arr):
    arr = np.array(arr)
    try:
        return np.linalg.det(arr)
    except np.linalg.LinAlgError as e:
        return f"Error: {e}"


# Function to calculate rank of a matrix
def rank(arr):
    arr = np.array(arr)
    try:
        return np.linalg.matrix_rank(arr)
    except np.linalg.LinAlgError as e:
        return f"Error: {e}"


# Function to calculate null space of a matrix
def nullSpace(arr):
    arr = np.array(arr)
    try:
        null_value = null_space(arr)
        return null_value.tolist()
    except LAerror as e:
        return f"Error: {e}"    


# Function to calculate eigenpairs
def eigenpairs(arr):
    arr = np.array(arr)
    try:
        eigenvalues, eigenvectors = np.eig(arr)
        return eigenvalues.tolist(), eigenvectors.tolist()
    except np.linalg.LinAlgError as e:
        return f"Error: {e}"


# Function to calculate LU decomposition
def LU(arr):
    arr = np.array(arr)
    try:
        P, L, U = lu(arr)
        return P.tolist(), L.tolist(), U.tolist()
    except LAerror as e:
        return f"Error: {e}"


# Function to calculate the singular value decomposition    
def SVD(arr):
    arr = np.array(arr)
    try:
        U, S, V = np.svd(arr)
        return U.tolist(), S.tolist(), V.tolist()
    except np.linalg.LinAlgError as e:
        return f"Error: {e}"
 

'''Gradio Interface to take input and show output'''

with gr.Blocks() as demo:
    gr.Markdown("NumPy Matrix Calculator")

    # For matrix addition, subtraction and multiplication
    with gr.Tab("Matrix Arithmetic"):
        input1 = gr.Dataframe(headers=None, row_count=3, col_count=3, label="Enter First Matrix")
        input2 = gr.Dataframe(headers=None, row_count=3, col_count=3, label="Enter Second Matrix")
        operation = gr.Radio(["Addition", "Subtraction", "Multiplication"], label="Select Operation")
        output = gr.Dataframe(headers=None, label="Output Matrix")
        button = gr.Button("Calculate")
        button.click(fn=matrix_arithmetic, inputs=[input1, input2, operation], outputs=output)


    # For transpose
    with gr.Tab("Transpose"):
        input = gr.Dataframe(headers=None, row_count=3, col_count=3, label="Enter Matrix")
        output = gr.Dataframe(headers=None, label="Output Matrix")
        button = gr.Button("Calculate")
        button.click(fn=transpose, inputs=[input], outputs=output)


    # For Inverse
    with gr.Tab("Inverse"):
        input = gr.DataFrame(headers=None, row_count=3, col_count=3, label= "Enter matrix")
        output = gr.DataFrame(headers=None, label="Output Matrix")
        button = gr.Button("Calculate")
        button.click(fn=inverse, inputs=[input], outputs=output)


    # For Determinant
    with gr.Tab("Determinant"):
        input = gr.DataFrame(headers=None, row_count=3, col_count=3, label= "Enter matrix")
        output = gr.Number(label="Determinant Value")
        button = gr.Button("Calculate")
        button.click(fn=determinant, inputs=[input], outputs=output)
    
    
    # For Rank
    with gr.Tab("Rank"):
        input = gr.DataFrame(headers=None, row_count=3, col_count=3, label= "Enter matrix")
        output = gr.Number(label="Rank Value")
        button = gr.Button("Calculate")
        button.click(fn=rank, inputs=[input], outputs=output)


    # For Null Space
    with gr.Tab("Null Space"):
        input = gr.DataFrame(headers=None, row_count=3, col_count=3, label= "Enter matrix")
        output = gr.DataFrame(headers=None, label="Output Matrix")
        button = gr.Button("Calculate")
        button.click(fn=nullSpace, inputs=[input], outputs=output)


    # For Eigenvalues and Eigenvectors
    with gr.Tab("Eigenvalues and Eigenvectors"):
        input = gr.DataFrame(headers=None, row_count=3, col_count=3, label="Enter matrix")
        output_value = gr.DataFrame(headers=None, label="Eigenvalues")
        output_matrix = gr.DataFrame(headers=None, label= "Eigenvectors")
        button = gr.Button("Calculate")
        button.click(fn=eigenpairs, inputs=input, outputs= [output_value,output_matrix])


    # For LU Decomposition
    with gr.Tab("LU Decomposition"):
        input = gr.DataFrame(headers=None, row_count=3, col_count=3, label= "Enter matrix")
        output1 = gr.DataFrame(headers=None, label="Permutation Matrix")
        output2 = gr.DataFrame(headers=None, label="Lower Matrix")
        output3 = gr.DataFrame(headers=None, label="Upper Matrix")
        button = gr.Button("Calculate")
        button.click(fn=LU, inputs=[input], outputs=[output1,output2,output3])


    # For SVD
    with gr.Tab("Singular Value Decomposition"):
        input = gr.DataFrame(headers=None, row_count=3, col_count=3, label= "Enter matrix")
        output1 = gr.DataFrame(headers=None, label="U")
        output2 = gr.DataFrame(headers=None, label="Sigma")
        output3 = gr.DataFrame(headers=None, label="VT")
        button = gr.Button("Calculate")
        button.click(fn=SVD, inputs=[input], outputs=[output1,output2,output3])

demo.launch()
