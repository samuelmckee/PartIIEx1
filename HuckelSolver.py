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

  #Make i and j no longer adjacent
  def remove_adjacent(self,i,j):
    if i < j :
      self.connections.discard( (i,j) )
    elif j < i :
      self.connections.discard( (j,i) )

