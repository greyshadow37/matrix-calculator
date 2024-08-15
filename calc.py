import numpy as np
import gradio as gr

#function to check whether matrix is square matrix
def square_matrix(arr):
    return len(arr) == len(arr[0])

#function to compare whether the dimensions of two matrices are equal
def matrix_dim(arr1,arr2):
    return np.shape(arr1) == np.shape(arr2)

#function for transpose
def transpose(arr):
    arr=np.array(arr)
    try:
        return np.transpose(arr)
    except np.linalg.LinAlgError as e:
        return f'error:{e}'

#operations on single matrix
def single_matrix(arr, oper):
    arr = np.array(arr)
    if not square_matrix(arr):
        return "Matrix is not square"
    try:
        if oper == "Determinant":
            return np.linalg.det(arr)
        elif oper == "Inverse":
            return np.linalg.inv(arr)
        elif oper == "Eigenvalues":
            return np.linalg.eigvals(arr)
        else:
            return "Error: Invalid operation"
    except np.linalg.LinAlgError as e:
        return f'error:{e}'
        
#operations on 2 matrices
def matrix_arithmetic(arr1,arr2,oper):
    arr1=np.array(arr1)
    arr2=np.array(arr2)
    if matrix_dim(arr1,arr2) == True:
        if oper == "Addition":
            return np.add(arr1,arr2)
        if oper == "Subtraction":
            return np.subtract(arr1,arr2)
        else:
            return "Error; Invalid operation"
    else:
        return "Error: Matrices have different dimensions"
    
#gradio interface
with gr.Blocks() as demo:
    gr.Markdown("NumPy Matrix Calculator")

#for transpose
    with gr.Tab("Transpose"):
        matrixt_input = gr.Dataframe(headers=None, row_count=3, col_count=3, label="Enter Matrix")
        transpose_output = gr.Dataframe(headers=None, label="Output Matrix")
        transpose_button = gr.Button("Calculate")
        transpose_button.click(fn=transpose, inputs=[matrixt_input], outputs=transpose_output)

#for single matrix
    with gr.Tab("Single Matrix Transformations"):
        matrix_input = gr.Dataframe(headers=None, row_count=3, col_count=3, label="Enter Matrix")
        operation_input = gr.Radio(["Determinant", "Inverse", "Eigenvalues"], label="Select Operation")
        single_matrix_output = gr.Textbox(label="Result")
        single_button = gr.Button("Calculate")
        single_button.click(fn=single_matrix, inputs=[matrix_input,  operation_input], outputs=single_matrix_output)

#for two matrices
    with gr.Tab("Matrix Arithmetic"):
        matrix1_input = gr.Dataframe(headers=None, row_count=3, col_count=3, label="Enter First Matrix")
        matrix2_input = gr.Dataframe(headers=None, row_count=3, col_count=3, label="Enter Second Matrix")
        operation_input_2 = gr.Radio(["Addition", "Subtraction"], label="Select Operation")
        arithmetic_output = gr.Dataframe(headers=None, label="Output Matrix")
        arithmetic_button = gr.Button("Calculate")
        arithmetic_button.click(fn=matrix_arithmetic, inputs=[matrix1_input, matrix2_input, operation_input_2], outputs=arithmetic_output)

demo.launch()