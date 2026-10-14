import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    if (len(x) != len(y)):
        return False
    dot_product = 0.0
    for i in range(len(x)):
        dot_product += x[i] * y[i]
    return dot_product
    