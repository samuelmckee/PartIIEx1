import molecule as mol

def generate_linear(n) :
  m = mol.Molecule(n)
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
  m = mol.Molecule(4)
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
  m = mol.Molecule(20)
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
