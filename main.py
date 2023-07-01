import pprint

import numpy as np
#import matplotlib.pyplot as plt
from File_fun import read_file
from Parsing_fun import parser
from Simulations import matrix_formulation_OP,matrix_formulation_AC
from Solution import Solve_Linear_Matrix


Circuit_Matrix = parser(read_file('Netlist_2.txt', list))

#Y, J = matrix_formulation_OP(Circuit_Matrix)
#print(Y,J)
#print(Solve_Linear_Matrix(Y, J))

v = []
for W in range(1,20):
    Y, J = matrix_formulation_AC(Circuit_Matrix,W)
    v.append(Solve_Linear_Matrix(Y, J))

print(v)