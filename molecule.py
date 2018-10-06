from numpy import zeros

#Stores the huckel matrix for a molecule with additional function for easily setting two atoms adjacent
class Molecule :
  num_atoms = 1              #Number of atoms in molecule
  huckel = zeros((1,1))   #Huckel matrix for molecule

  def __init__(self, n) :
    if n < 1:      # A molecule object must have at least 1 atom
      raise ValueError('Must enter a positive integer')
    else:
      self.num_atoms = n
      self.huckel = zeros((n,n))  #Create n x n huckel matrix

  #Make atoms i and j adjacent
  def add_adjacent(self,i,j):
    if i < 0 or j < 0 or i >= self.num_atoms or j >= self.num_atoms: 
      print('Invalid atoms')
    elif i == j :
      print('Cannot connect atom to itself')
    else :
      self.huckel[i,j] = -1
      self.huckel[j,i] = -1

