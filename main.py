from numpy.linalg import eigvals
from mol_gen import *
from utils import *

while 1 :
  print("Select a type of molecule (enter number)")
  print("1. Linear polyene with n carbons")
  print("2. Cyclic polyene with n carbons")
  print("3. Tetrahedron")
  print("4. Cube")
  print("5. Dodecahedron")
  print("6. Octohedron")
  print("7. Icosahedron")
  print("8. Buckminsterfullerene")
  print("9. Exit")

  choice = get_int("Enter your selection: ", "Selection must be from list: ", lambda x: x in [1,2,3,4,5,6,7,8,9])

  #lambda functions that return molecule object of desired type
  switcher = {
      1: lambda: generate_linear(get_int("Enter number of atoms in chain: ", "Input must be integer greater than 1: ", lambda x : x > 1)),
      2: lambda: generate_cyclic(get_int("Enter number of atoms in ring: ", "Input must be integer greater than 2: ", lambda x : x > 2)),
      3: lambda: generate_tetrahedron(),
      4: lambda: generate_cube(),
      5: lambda: generate_dodecahedron(),
      6: lambda: generate_octahedron(),
      7: lambda: generate_icosahedron(),
      8: lambda: generate_c60()
    }

  if choice == 9 :  #User selected exit
    break
  else :
    m = switcher.get(choice)()           #Retrieve and run lambda function from switcher to get molecule object
    evals = eigvals(m.huckel)  #Extract stored matrix from molecule and calculate eigenvalues
    print_evals(evals)             #Output results
