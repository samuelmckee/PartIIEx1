from molecule import *

#This file contains functions for generating preset molecule objects"

def generate_linear(n) :
  m = Molecule(n)
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
  m = Molecule(4)
  for i in range(0,4) :
   for j in range(i,4) :
    if not i==j :
      m.add_adjacent(i, j)
  return m


def generate_cube():
  #Start with 2 x 4 member rings and add links across to form cube
  m = Molecule(8)
  for i in range(0,3) :
    m.add_adjacent(i,i+1)
    m.add_adjacent(i+4,i+5)
  m.add_adjacent(0,3)
  m.add_adjacent(4,7)

  for i in range(0,4) :
    m.add_adjacent(i, i+4)

  return m


def generate_dodecahedron():
  m = Molecule(20)

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


def generate_octahedron() :
  m = Molecule(6)

  #Generate 4 member ring
  for i in range(0,3) :
    m.add_adjacent(i,i+1)
  m.add_adjacent(0,3)

  #Add additional atoms above and below ring to form octohedron
  for i in range(0,4) :
    m.add_adjacent(i,4)
    m.add_adjacent(i,5)

  return m


def generate_icosahedron() :
  m = Molecule(12)

  #Connections are added starting at top of molecule and working down, 1 plane of atoms at a time
  for i in range(1,6) :
    m.add_adjacent(0,i)

  for i in range(1,5) :
    m.add_adjacent(i,i+1)
  m.add_adjacent(1,5)

  for i in range(1,5) :
    m.add_adjacent(i, i+5)
    m.add_adjacent(i, i+6)
  m.add_adjacent(5,6)
  m.add_adjacent(5,10)

  for i in range(6,10) :
    m.add_adjacent(i,i+1)
  m.add_adjacent(6,10)

  for i in range(6,11) :
    m.add_adjacent(i,11)

  return m


def generate_c60() :
  m = Molecule(60)

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

