import numpy as np
import mol_gen as gen
import utils

while 1 :
  print("Select a type of molecule (enter number)")
  print("1. Linear polyene with n carbons")
  print("2. Cyclic polyene with n carbons")
  print("3. Tetrahedron")
  print("4. Cube")
  print("5. Dodecahedron")
  print("6. Buckminsterfullerene")
  print("7. Exit")

  choice = utils.get_int("Enter your selection: ", "Selection must be from list: ", lambda x: x in [1,2,3,4,5,6,7])

  #lambda functions that return molecule object of desired type
  switcher = {
      1: lambda: gen.generate_linear(utils.get_int("Enter number of atoms in chain: ", "Input must be integer greater than 1: ", lambda x : x > 1)),
      2: lambda: gen.generate_cyclic(utils.get_int("Enter number of atoms in ring: ", "Input must be integer greater than 2: ", lambda x : x > 2)),
      3: lambda: gen.generate_tetrahedron(),
      4: lambda: gen.generate_cube(),
      5: lambda: gen.generate_dodecahedron(),
      6: lambda: gen.generate_c60()
    }

  if choice == 7 :  #User selected exit
    break
  else :
    m = switcher.get(choice)()           #Retrieve and run lambda function from switcher to get molecule object
    evals = np.linalg.eigvals(m.huckel)  #Extract stored matrix from molecule and calculate eigenvalues
    utils.print_evals(evals)             #Output results
