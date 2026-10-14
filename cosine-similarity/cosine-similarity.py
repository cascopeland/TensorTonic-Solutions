import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    numerator = np.dot(a, b)
    a_denominator = np.linalg.norm(a)
    b_denominator = np.linalg.norm(b)
    if (a_denominator == 0 or b_denominator == 0):
        return 0.0
    cross_denom = a_denominator * b_denominator
    return float(numerator/cross_denom)
    