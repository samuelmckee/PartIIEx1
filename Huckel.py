import numpy as np
import math

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
  for i in range(0,4) :
    m.add_adjacent(i,i+1)
    m.add_adjacent(i+15,i+16)
  m.add_adjacent(0,4)
  m.add_adjacent(15,19)

  #Connect top and bottom layer to middle layers
  for i in range(0,5) :
    m.add_adjacent(i, i+5)
    m.add_adjacent(i+10, i+15)

  #Connect two middle layers together
  for i in range(5, 9) :
    m.add_adjacent(i, i + 5)
    m.add_adjacent(i, i + 6)
  m.add_adjacent(9,10)
  m.add_adjacent(9,14)
  return m

def print_evals(evals):
  print()
  print("-------------------------")
  print("Degeneracy  |  Eigenvalue")
  print("------------|------------")
  evals.sort()
  current_eval = evals[0]  #Eigenvalue currently being checked for degeneracy
  degeneracy = 1   #Degeneracy of current eigenvalue
  for eval in evals[1:]:
    if math.isclose(eval, current_eval, abs_tol=1e-10) :  #Checks if two eigenvalues are within given tolerance
      degeneracy += 1
    else :
      print ("{: 10d}  | {: 2.8f}".format(degeneracy, current_eval))
      current_eval = eval
      degeneracy = 1
  print ("{: 10d}  | {: 2.8f}".format(degeneracy, current_eval))
  print("-------------------------") 
  print()

#Reads user input until an integer is entered
def get_int(message):
  user_input = input(message)
  while 1 :
    try :
      return int(user_input)
    except ValueError :
      user_input = input("Input must be an integer: ")

#Reads user input until a positive integer is entered
def get_pos_int(message):
  while 1 :
    user_input = get_int(message)
    if user_input > 0 :
      return user_input
    else :
      user_input = get_int("Input must be positive: ")

#Main function of program begins here
while 1 :
  print("Select a type of molecule (enter number)")
  print("1. Linear polyene with n carbons")
  print("2. Cyclic polyene with n carbons")
  print("3. Tetrahedron")
  print("4. Cube")
  print("5. Dodecahedron")
  print("6. Exit")

  choice = get_int("Enter your selection: ")
  while choice not in [1,2,3,4,5,6]:
    choice = get_int("Selection must be from the list: ")

  switcher = {
      1: lambda: generate_linear(get_pos_int("Enter number of atoms in chain: ")),
      2: lambda: generate_cyclic(get_pos_int("Enter number of atoms in ring: ")),
      3: lambda: generate_tetrahedron(),
      4: lambda: generate_cube(),
      5: lambda: generate_dodecahedron()
    }

  if choice == 6 :
    break
  else :
    m = switcher.get(choice)()
    evals = np.linalg.eigvals(m.huckel)
    print_evals(evals)
