from typing import List, Dict
import pprint
from File_fun import read_file
from Parsing_fun import parser
from Simulations import matrix_formulation

#pprint.pprint(parser(read_file('Netlist_1.txt', list)))

A = parser(read_file('Netlist_1.txt', list))

print(matrix_formulation(A))