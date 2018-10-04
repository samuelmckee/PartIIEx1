import numpy as np

def generate_linear (n, alpha, beta)
  #Generate matrix with diagonal entries set to alpha value
  huckel = np.identity(n)
  huckel *= alpha

  #Set matrix elements for adjacent atoms to beta
  for i in range(0,n - 1) :
    huckel[i,i+1] = beta
    huckel[i+1,i] = beta
  return huckel

def generate_cyclic (n, alpha, beta)
  #Start out with linear polyene, then join the ends to account for ring 
  huckel = generate_linear(n, alpha, beta)
  huckel[0,n-1] = beta
  huckel[n-1,0] = beta
  return huckel

