import numpy as np

def linear_forward_test_case():
    np.random.seed(1)
    A=np.random.randn(3,2)
    W=np.random.randn(1,3)
    b=np.random.randn(1,1)
    return A,W,b