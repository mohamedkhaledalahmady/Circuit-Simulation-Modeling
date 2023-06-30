import pprint
from File_fun import read_file
from Parsing_fun import parser
from Simulations import matrix_formulation
from Solution import Solve_Linear_Matrix


Circuit_Matrix = parser(read_file('Netlist_1.txt', list))
Y, J = matrix_formulation(Circuit_Matrix)
print(Solve_Linear_Matrix(Y, J))
