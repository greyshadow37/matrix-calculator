import numpy as np

def square_matrix(arr):
    return len(arr) == len(arr[0])

def matrix_dim(arr1,arr2):
    return np.shape(arr1) == np.shape(arr2)
    
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

def two_matrix(arr1,arr2,oper):
    if oper == 1:
        return np.add(arr1,arr2)
    if oper == 2:
        return np.subtract(arr1,arr2)
    else:
        return "Error; Invalid operation"
    
    
def master():
    
    nmat=int(input('''1. Single matrix operations (square matrices only)
2. Two matrix operations (matrices should be of same dimension)
'''))
    
    if nmat==1:
        dim=int(input('Enter the dimensions of the square matrix:\n'))
        l=[]
        for i in range(dim):
            st=input(f'Enter the {i+1}th row seperated by commas:\n')
            temp = [int(x) for x in st.split(',')]
            l.append(temp)
        
        if not square_matrix(l):
            return "Error: Matrix is not square"

        #converting to numpy array
        l=np.array(l)
        
        #taking choice of operation as input
        choice=int(input('''1. Transpose
2. Determinant
3. Inverse
4. Eigenvalues
                     '''))
        print(single_matrix(l,choice))

    if nmat==2:
        dim=int(input('Enter the number of rows of the matrices:\n'))
        l1=[]
        l2=[]
        for i in range(dim):
            st=input(f'Enter {i+1}th the row of the 1st matrix seperated by commas:\n')
            temp = [int(x) for x in st.split(',')]
            l1.append(temp)
        
        for i in range(dim):
            st=input(f'Enter the {i+1}th row of the 2nd matrix seperated by commas:\n')
            temp = [int(x) for x in st.split(',')]
            l2.append(temp)
        
        
        # condition to check whether matrix dimensions are same or not 
        if not matrix_dim(l1, l2):
            return "Error: Matrices have different dimensions"
    
        #converting to numpy arrays
        l1=np.array(l1)
        l2=np.array(l2)

        #taking choice of operation as input
        choice=int(input('''1. Addition 
2. Substraction
                     '''))
        
        print(two_matrix(l1,l2,choice)) 
    

if __name__ == "__main__":
    master()