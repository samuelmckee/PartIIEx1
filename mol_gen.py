import molecule as mol

#This file contains functions for generating preset molecule objects"

def generate_linear(n) :
  m = mol.Molecule(n)
  for i in range(0,n-1) :
    m.add_adjacent(i, i+1)
  return m

def generate_cyclic(n) :
  #Start with linear polyene, then link ends together
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
  m = mol.Molecule(20)

  #Connections are added starting at top of molecule and working down, 1 plane of atoms at a time
  for i in range(0,4) :
    m.add_adjacent(i,i+1)
  m.add_adjacent(0,4)

  for i in range(0,5) :
    m.add_adjacent(i, i+5)

  for i in range(5, 9) :
    m.add_adjacent(i, i + 5)
    m.add_adjacent(i, i + 6)
  m.add_adjacent(9,10)
  m.add_adjacent(9,14)

  for i in range(10,15) :
    m.add_adjacent(i, i+5)

  for i in range(15,19) :
    m.add_adjacent(i, i+1)
  m.add_adjacent(15,19)

  return m

def generate_c60() :
  m = mol.Molecule(60)

  #Connection are added starting at top of molecule and working down, 1 plane of atoms at a time
  for i in range(0,4) :
    m.add_adjacent(i,i+1)
  m.add_adjacent(0,4)

  for i in range(0,5) :
    m.add_adjacent(i,i+5)

  for i in range(6,10) :
    m.add_adjacent(i, 2 * i - 1)
    m.add_adjacent(i, 2 * i)
  m.add_adjacent(5,10)
  m.add_adjacent(5,19)

  for i in range(5,10) :
    m.add_adjacent(2 * i, 2 * i + 1)

  for i in range(10, 20) :
    m.add_adjacent(i,i+10)

  for i in range(11,15) :
    m.add_adjacent(2 * i - 1, 2 * i)
  m.add_adjacent(20,29)

  for i in range(20,30) : 
    m.add_adjacent(i, i+10)

  for i in range(15,20) :
    m.add_adjacent(2 * i, 2 * i + 1)

  for i in range(30,40) :
    m.add_adjacent(i, i+10)

  for i in range(21,25) :
    m.add_adjacent(2 * i - 1, 2 * i)
  m.add_adjacent(40,49)

  for i in range(20,25) :
    m.add_adjacent(2 * i    , i + 30)
    m.add_adjacent(2 * i + 1, i + 30)

  for i in range(50,55) :
    m.add_adjacent(i, i+5)

  for i in range(55,59) :
    m.add_adjacent(i, i+1)
  m.add_adjacent(55, 59)

  return m

