import pprint
import numpy as np
import matplotlib.pyplot as plt
from File_fun import read_file
from Parsing_fun import parser
from Simulations import matrix_formulation_OP, matrix_formulation_AC
from Solution import Solve_Linear_Matrix

Circuit_Matrix = parser(read_file('Netlist_1.txt', list))
########################### DC Analysis ########################### 
Y, J = matrix_formulation_OP(Circuit_Matrix)
print(Solve_Linear_Matrix(Y, J))

# TODO: Know which Analysis is required from Netlist

########################### AC Analysis ########################### 
# n = Circuit_Matrix["num_nets"] + Circuit_Matrix["vsource_list"].__len__()
# from_frequency = 1
# to_frequency = 1000
# number_of_frequencies = 500
# # TODO: Get These Data (frequencies rang) from Netlist
# v = np.zeros([n, number_of_frequencies])
# frequencies = np.linspace(start=from_frequency, stop=to_frequency, num=number_of_frequencies)
# i = 0
# for frq in frequencies:
#     Y, J = matrix_formulation_AC(Circuit_Matrix, frq)
#     v[:, i, np.newaxis] = Solve_Linear_Matrix(Y, J)
#     i += 1

# plt.plot(frequencies, 20*np.log10(v[1, :]), 'r')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Amplitude (dB)')
# plt.title('Vout Frequency Response')
# plt.xscale('log')
# plt.grid(True)
# plt.show()
