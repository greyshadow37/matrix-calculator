import numpy as np
import gradio as gr

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

#for two matrices
    with gr.Tab("Matrix Arithmetic"):
        matrix1_input = gr.Dataframe(headers=None, row_count=3, col_count=3, label="Enter First Matrix")
        matrix2_input = gr.Dataframe(headers=None, row_count=3, col_count=3, label="Enter Second Matrix")
        operation_input_2 = gr.Radio(["Addition", "Subtraction"], label="Select Operation")
        arithmetic_output = gr.Dataframe(headers=None, label="Output Matrix")
        arithmetic_button = gr.Button("Calculate")
        arithmetic_button.click(fn=matrix_arithmetic, inputs=[matrix1_input, matrix2_input, operation_input_2], outputs=arithmetic_output)

demo.launch()
