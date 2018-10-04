import numpy as np

class Molecule :
  #Number of atoms in molecule
  num_atoms = 1
  #Set containing connections between adjacent atoms
  connections = set()

  def __init__(self, n) :
    # A molecule object must have at least 1 atom
    if n < 1:
      raise ValueError('Must enter a positive integer')
    else:
      self.num_atoms = n

  #Make atoms i and j adjacent
  def add_adjacent(self,i,j):
    if i < 0 or j < 0 or i >= self.num_atoms or j >= self.num_atoms: 
      print('Invalid atoms')
    elif i < j :
      self.connections.add((i,j))
    elif j < i :
      self.connections.add((j,i))
    else:
      # i = j. Atom cannot connect to itself
      print('Cannot connect atom to itself')

  #Generate huckel matrix for molecule object
  def generate_huckel(self, alpha, beta) :
    #Generate matrix with diagonal entries set to alpha value
    huckel = np.identity(self.num_atoms)
    huckel *= alpha

    #Set matrix elements for adjacent atoms to beta
    for (i,j) in self.connections:
      huckel[i,j] = beta
      huckel[j,i] = beta
    return huckel


def generate_linear(n) :
  m = Molecule(n)
  for i in range(0,n-1) :
    m.add_adjacent(i, i+1)
  return m

def generate_cyclic(n) :
  #Start with linear poly-ene, then link ends together
  m = generate_linear(n)
  m.add_adjacent(0, n-1)
  return m


