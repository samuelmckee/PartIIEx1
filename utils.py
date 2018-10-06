from math import isclose

#Reads user input until integer meeting predicate is supplied
def get_int(message, err_message, pred):
  user_input = input(message)
  while 1 :
    try :
      int_value = int(user_input)
      if pred(int_value) :
        return int_value
      else :
        user_input = input(err_message)
    except ValueError :
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
    if isclose(eval, current_eval, abs_tol=1e-10) :  #Checks if two eigenvalues are within given tolerance (and counts them as degenerate if they are)
      degeneracy += 1                                     #Increment degeneracy for current eigenvalue
    else :
      print ("{: 10d}  | {: 2.8f}".format(degeneracy, current_eval))  #Print current eigenvalue/degeneracy and begin processing next eigenvalue
      current_eval = eval
      degeneracy = 1
  print ("{: 10d}  | {: 2.8f}".format(degeneracy, current_eval))
  print("-------------------------") 
  print()

