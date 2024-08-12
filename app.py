import numpy as np
import gradio as gr
import calc


#gradio components
nmat= gr.Dropdown(
    ["Single matrix Operation", "Two Matrix Operation"],
    label="Choose the type of Operations"
)

l1=gr.DataFrame(
    label="Enter Matrix 1",
    type="array",
    visible=False
)

l2=gr.DataFrame(
    label="Enter Matrix 2",
    type="array",
    visible=False
)

op1=gr.Dropdown(
    label="Enter the Operation",
    choices=["Transpose","Determinant","Inverse","Eigenvalues"],
    visible=False
)

op2=gr.Dropdown(
    label="Enter the Operation",
    choices=["Addition","Subtraction"],
    visible=False
)


