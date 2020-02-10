import numpy as np
import nbtw

def star_graph(n):
    A = np.zeros((n,n))
    for ii in range(1,n):
        A[0,ii] = 1
        A[ii,0] = 1
    return A

def complete_graph(n):
    return np.ones((n,n))-np.identity(n)

print('All pairwise NBTWs for the star graph, n = 4, k = 2')
print(nbtw.get_nbtws(star_graph(4),2))
print('Some example values for the complete graph, between nodes 1-1 and 1-2:')
print('n = 6, k = 8:    1-1: '+str(nbtw.get_nbtws(complete_graph(6),8)[0,0])+', 1-2: '+str(nbtw.get_nbtws(complete_graph(6),8)[0,1]))
print('n = 8, k = 7:    1-1: '+str(nbtw.get_nbtws(complete_graph(8),7)[0,0])+', 1-2: '+str(nbtw.get_nbtws(complete_graph(8),7)[0,1]))
print('n = 10, k = 6:   1-1: '+str(nbtw.get_nbtws(complete_graph(10),6)[0,0])+', 1-2: '+str(nbtw.get_nbtws(complete_graph(10),6)[0,1]))
