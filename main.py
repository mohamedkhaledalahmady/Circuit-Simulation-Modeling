import pprint
import numpy as np
import matplotlib.pyplot as plt
from File_fun import read_file
from Parsing_fun import parser
from Simulations import matrix_formulation_OP, matrix_formulation_AC
from Solution import Solve_Linear_Matrix


Circuit_Matrix = parser(read_file('Netlist_2.txt', list))
# Y, J = matrix_formulation_OP(Circuit_Matrix)
# print(Solve_Linear_Matrix(Y, J))

n = Circuit_Matrix["num_nets"]
v = np.zeros([n, 19])
print(v.shape)
for W in range(1, 20):
    Y, J = matrix_formulation_AC(Circuit_Matrix, W)
    # v.append(Solve_Linear_Matrix(Y, J))
    v[:, W] = Solve_Linear_Matrix(Y, J)

# plt.plot(np.abs(v), range(1, 20))

print(v)
print(len(v))
