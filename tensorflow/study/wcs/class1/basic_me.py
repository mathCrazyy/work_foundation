import numpy as np
def np_sigmoid(x):
    """
    compute sigmoid x vector
    Argument :
    x -- a vector or matrix
    return s
    s --sigmoid(x)
    """
    s=1/(np.exp(-x)+1)
    return s