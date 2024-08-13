import numpy as np
import gradio as gr
import calc


def calculate(nmat, l1, l2, op1, op2):
    try:
        if nmat == "Single matrix Operation":
            if calc.square_matrix(l1):
                return calc.single_matrix(l1, op1)
            else:
                return "Matrix is not square"
        elif nmat == "Two Matrix Operation":
            if calc.matrix_dim(l1, l2):
                return calc.two_matrix(l1, l2, op2)
            else:
                return "Matrix dimensions are not equal"
        else:
            return "Invalid Input"
    except Exception as e:
        return str(e)
    


with gr.Blocks() as demo:
    nmat = gr.Dropdown(
        ["Single matrix Operation", "Two Matrix Operation"],
        label="Choose the type of Operations"
    )
    l1 = gr.DataFrame(
        label="Enter Matrix 1",
        type="array",
        visible=False
    )
    
    l2 = gr.DataFrame(
        label="Enter Matrix 2",
        type="array",
        visible=False
    )
    
    op1 = gr.Radio(
        label="Select Operation for Single Matrix",
        choices=["Transpose", "Determinant", "Inverse", "Eigenvalues"],
        visible=False
    )

    op2 = gr.Radio(
        label="Select Operation for Two Matrices",
        choices=["Addition", "Subtraction"],
        visible=False
    )
    result = gr.Textbox(label="Result")
    def update_visibility(nmat):
        if nmat == "Single matrix Operation":
            l2.visible = False
            op2.visible = False
            op1.visible = True
        elif nmat == "Two Matrix Operation":
            l2.visible = True
            op2.visible = True
            op1.visible = False
        else:
            l2.visible = False
            op2.visible = False
            op1.visible = False

    nmat.change(update_visibility)
    
    def on_change(nmat):
        update_visibility(nmat)
        return gr.update()
    nmat.change(on_change)
    
    calculate_button = gr.Button("Calculate")
    
    calculate_button.click(
        calculate,
        inputs=[nmat, l1, l2, op1, op2],
        outputs=result
    )
    
demo.launch(share=True)
