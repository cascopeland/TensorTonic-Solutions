import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here

    temp = np.zeros((len(A[0]), len(A)))
    for i in range(len(A)):
        for j in range(len(A[i])):
            temp[j][i] = A[i][j]
    return temp
