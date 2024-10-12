import numpy as np
import gradio as gr

# Function to compare whether the dimensions of two matrices are equal
def matrix_dim(arr1, arr2):
    return np.shape(arr1) == np.shape(arr2)

# Function for transpose
def transpose(arr):
    arr = np.array(arr)
    try:
        return np.transpose(arr)
    except np.linalg.LinAlgError as e:
        return f'error: {e}'
        
# Operations on 2 matrices
def matrix_arithmetic(arr1, arr2, oper):
    arr1 = np.array(arr1, dtype=float)
    arr2 = np.array(arr2, dtype=float)

    print("Matrix 1 shape:", arr1.shape)  
    print("Matrix 2 shape:", arr2.shape)  

    if oper == "Multiplication":
        if arr1.shape[1] == arr2.shape[0]:  # Check if multiplication is possible
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
    
# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("NumPy Matrix Calculator")

    # For transpose
    with gr.Tab("Transpose"):
        matrixt_input = gr.Dataframe(headers=None, row_count=3, col_count=3, label="Enter Matrix")
        transpose_output = gr.Dataframe(headers=None, label="Output Matrix")
        transpose_button = gr.Button("Calculate")
        transpose_button.click(fn=transpose, inputs=[matrixt_input], outputs=transpose_output)

    # For two matrices
    with gr.Tab("Matrix Arithmetic"):
        matrix1_input = gr.Dataframe(headers=None, row_count=3, col_count=3, label="Enter First Matrix")
        matrix2_input = gr.Dataframe(headers=None, row_count=3, col_count=3, label="Enter Second Matrix")
        operation_input_2 = gr.Radio(["Addition", "Subtraction", "Multiplication"], label="Select Operation")
        arithmetic_output = gr.Dataframe(headers=None, label="Output Matrix")
        arithmetic_button = gr.Button("Calculate")
        arithmetic_button.click(fn=matrix_arithmetic, inputs=[matrix1_input, matrix2_input, operation_input_2], outputs=arithmetic_output)

demo.launch()
