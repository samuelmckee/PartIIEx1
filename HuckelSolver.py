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

def generate_tetrahedron():
  #All atoms connected to all other atoms
  m = Molecule(4)
  for i in range(0,4) :
   for j in range(i,4) :
    if not i==j :
      m.add_adjacent(i, j)
  return m

def generate_cube():
  #Start with 8 member ring and add links across to form cube
  m = generate_cyclic(8)
  m.add_adjacent(0,3)
  m.add_adjacent(4,7)
  m.add_adjacent(2,5)
  m.add_adjacent(1,6)
  return m

def generate_dodecahedron():
  #Start with empty 20 point molecule
  m = Molecule(20)
  #Dodecahedron is split into planes of atoms, which are added sequentially
  #Top and bottom layers are 5 member rings
  for i in range(0,4) :
    m.add_adjacent(i,i+1)
    m.add_adjacent(i+15,i+16)
  m.add_adjacent(0,4)
  m.add_adjacent(15,19)

  #Connect top and bottom layer to middle layers
  for i in range(0,5) :
    m.add_adjacent(i, i+5)
    m.add_adjacent(i+15, i+10)

  #Connect two middle layers together
  for i in range(0, 4) :
    m.add_adjacent(i + 5, i + 10)
    m.add_adjacent(i + 6, i + 10)
  m.add_adjacent(5,14)
  m.add_adjacent(9,14)
  return m
