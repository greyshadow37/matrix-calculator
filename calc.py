import numpy as np

def single_matrix(arr,oper):
    arr = np.array(arr)
    if oper == 1:
        return np.linalg.det(arr)
    if oper == 2:
        return np.linalg.inv(arr)
    if oper == 3:
        return np.linalg.eigvals(arr)
    else:
        return "Error; Invalid operation"
    

def two_matrix(arr1,arr2,oper):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    if oper == 1:
        return np.add(arr1,arr2)
    if oper == 2:
        return np.subtract(arr1,arr2)
    else:
        return "Error; Invalid operation"
    
    
def matrix_input():
    nmat=int(input('''1. Single matrix operations (square matrices only)
2. Two matrix operations (matrices should be of same dimension)
'''))
    
    
    if nmat==1:
        dim=int(input('Enter the dimensions of the square matrix:\n'))
        l=[]
        for i in range(dim):
            st=input('Enter the row seperated by commas:\n')
            temp = [int(x) for x in st.split(',')]
            l.append(temp)
        choice=int(input('''1. Determinant
2. Inverse
3. Eigenvalues
                     '''))
        print(single_matrix(l,choice))

    if nmat==2:
        dim=int(input('Enter the number of rows of the matrices:\n'))
        l1=[],l2=[]
        for i in range(dim):
            st=input('Enter the row seperated by commas:\n')
            temp = [int(x) for x in st.split(',')]
            l1.append(temp)
        
        for i in range(dim):
            st=input('Enter the row seperated by commas:\n')
            temp = [int(x) for x in st.split(',')]
            l2.append(temp)
        
        choice=int(input('''1. Addition 
2. Substraction
                     '''))
        print(two_matrix(l1,l2,choice)) 
    
    else:
        print('''invalid option
please try again
                ''')
        matrix_input()

matrix_input()