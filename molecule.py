import numpy as np

class Molecule :
  num_atoms = 1              #Number of atoms in molecule
  huckel = np.zeros((1,1))   #Set containing connections between adjacent atoms

  def __init__(self, n) :
    if n < 1:      # A molecule object must have at least 1 atom
      raise ValueError('Must enter a positive integer')
    else:
      self.num_atoms = n
      self.huckel = np.zeros((n,n))
  
  #Make atoms i and j adjacent
  def add_adjacent(self,i,j):
    if i < 0 or j < 0 or i >= self.num_atoms or j >= self.num_atoms: 
      print('Invalid atoms')
    elif i == j :
      print('Cannot connect atom to itself')
    else :
      self.huckel[i,j] = -1
      self.huckel[j,i] = -1

