import pprint
import numpy as np
import matplotlib.pyplot as plt
from File_fun import read_file
from Parsing_fun import parser
from Simulations import matrix_formulation_OP, matrix_formulation_AC
from Element_stamps import Convert_unit_to_value
from Solution import Solve_Linear_Matrix

########################### Netlist Parsing ####################### 
Circuit_Matrix = parser(read_file('Netlist_2.txt', list))
pprint.pprint(Circuit_Matrix)

if Circuit_Matrix["analysis"][0]["analysis_type"] == "dc":
########################### DC Analysis ########################### 
    Y, J = matrix_formulation_OP(Circuit_Matrix)
    print(Solve_Linear_Matrix(Y, J))

elif Circuit_Matrix["analysis"][0]["analysis_type"] == "ac":
########################### AC Analysis ########################### 
    n = Circuit_Matrix["num_nets"] + Circuit_Matrix["vsource_list"].__len__()
    from_frequency = Circuit_Matrix["analysis"][0]["freq_start"] * Convert_unit_to_value[Circuit_Matrix["analysis"][0]["freq_start_unit"]]
    to_frequency = Circuit_Matrix["analysis"][0]["freq_stop"] * Convert_unit_to_value[Circuit_Matrix["analysis"][0]["freq_stop_unit"]]
    number_of_decades = int(np.log10(to_frequency/from_frequency))
    number_of_frequencies = Circuit_Matrix["analysis"][0]["points_per_dec"]*number_of_decades
    v = np.zeros([n, number_of_frequencies])
    frequencies = np.linspace(start=from_frequency, stop=to_frequency, num=number_of_frequencies)
    i = 0
    for frq in frequencies:
        Y, J = matrix_formulation_AC(Circuit_Matrix, frq)
        v[:, i, np.newaxis] = Solve_Linear_Matrix(Y, J)
        i += 1

    plt.plot(frequencies, 20*np.log10(v[3, :]), 'r')
    # plt.plot(frequencies, v[3, :], 'r')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Parallel Resonant BPF')
    plt.xscale('log')
    plt.grid(True)
    plt.show()
