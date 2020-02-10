import numpy as np

def get_nbtws(A,k):
    # A: numpy matrix
    # k: int (>= 0)
    assert len(A.shape) == 2 and A.shape[0] == A.shape[1]
    assert np.allclose(A.T,A)
    assert k >= 1
    if k == 0:
        return np.identity(A.shape[0]) # one self-walk of length 0 by definition
    if k == 1:
        return A
    D = np.diag(np.matmul(A,np.ones(A.shape[0])))
    P = []
    P.append(A)
    P.append(np.matmul(A,A)-D)
    for ii in range(2,k):
        P.append(np.matmul(A,P[1]) - np.matmul((D-np.identity(A.shape[0])),P[0]))
        P.pop(0)
    return P[1]
