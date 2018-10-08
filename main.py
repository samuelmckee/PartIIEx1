from numpy.linalg import eigvals
from mol_gen import *
from math import isclose

#Reads user input until integer meeting predicate is supplied
def get_int(message, err_message, pred):
    user_input = input(message)
    while 1:
        try:
            int_value = int(user_input)
            if pred(int_value):
                return int_value
            else:
                user_input = input(err_message)
        except ValueError:
            user_input = input(err_message)

#Takes list of eigenvalues and prints it to console with degeneracies
def print_evals(evals):
    print()
    print("-------------------------")
    print("Degeneracy  |  Eigenvalue")
    print("------------|------------")
    evals.sort()
    current_eval = evals[0]  #Eigenvalue currently being checked for degeneracy
    degeneracy = 1           #Degeneracy of current eigenvalue
    for eval in evals[1:]:
        if isclose(eval, current_eval, abs_tol=1e-10):  #Checks if two eigenvalues are within given tolerance (and counts them as degenerate if they are)
            degeneracy += 1                              #Increment degeneracy for current eigenvalue
        else:
            print ("{: 10d}  | {: 2.8f}".format(degeneracy, current_eval))  #Print current eigenvalue/degeneracy and begin processing next eigenvalue
            current_eval = eval
            degeneracy = 1
    print("{: 10d}  | {: 2.8f}".format(degeneracy, current_eval))
    print("-------------------------") 
    print()


while 1:
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

    #functions to return molecule object of desired type
    switcher = {
        1: lambda: generate_linear(get_int("Enter number of atoms in chain: ", "Input must be integer greater than 1: ", lambda x : x > 1)),
        2: lambda: generate_cyclic(get_int("Enter number of atoms in ring: ", "Input must be integer greater than 2: ", lambda x : x > 2)),
        3: generate_tetrahedron,
        4: generate_cube,
        5: generate_dodecahedron,
        6: generate_octahedron,
        7: generate_icosahedron,
        8: generate_c60
    }

    if choice == 9:  #User selected exit
        break
    else:
        m = switcher.get(choice)()  #Retrieve and run function from switcher to get molecule object
        evals = eigvals(m.huckel)   #Get stored matrix from molecule and calculate eigenvalues
        print_evals(evals)          #Output results
