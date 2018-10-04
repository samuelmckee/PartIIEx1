import numpy as np
import itertools as iter
alpha = 0
beta = -1.

class Molecule:
  #List of
  num_atoms = 1
  connections = []
  def __init__(self, n):
    if n < 1 :
      raise ValueError('Must enter a positive integer')
    else :
      self.num_atoms = n
  
