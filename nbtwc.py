import numpy as np

def get_nbtw_centrality(A,k):
    # A: numpy matrix
    # k: int (natural)
    assert len(A.shape) == 2 and A.shape[0] == A.shape[1]
    assert np.allclose(A.T,A)
    D = np.diag(np.matmul(A,np.ones(A.shape[0])))
    P = []
    P.append(A)
    P.append(np.matmul(A,A)-D)
    for ii in range(2,k):
        P.append(np.matmul(A,P[ii-1]) - np.matmul((D-np.identity(A.shape[0])),P[ii-2]))
    return P[-1]
