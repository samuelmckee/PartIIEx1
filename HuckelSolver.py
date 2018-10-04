import numpy as np

n = 10
alpha = 0.
beta = -1.

#Generate matrix with diagonal elements set to alpha value
  huckel = np.identity[n]
  huckel *= alpha
#Set matrix elements for adjecent atoms equal to beta value

#Make atoms i and j adjacent
def add_adjacent(huckel, i, j, beta):
  if i = j :
    # i = j. Atom cannot connect to itself
    print('Cannot connect atom to itself')
  else :
    huckel[i,j] = beta
    huckel[j,i] = beta
