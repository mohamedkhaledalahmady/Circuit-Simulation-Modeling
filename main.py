import pprint
import numpy as np
from File_fun import read_file
from Parsing_fun import parser
from Simulations import *
from Element_stamps import Convert_unit_to_value
from Solution import Solve_Linear_Matrix

########################### Netlist Parsing ####################### 
Circuit_Matrix = parser(read_file('Netlist_2.txt', list))
# pprint.pprint(Circuit_Matrix)

# TODO : try and catch must be implemented here (if netlist not correct)
if Circuit_Matrix["analysis"][0]["analysis_type"] == "dc":
########################### DC Analysis ###########################
    Y, V, J = matrix_formulation_OP(Circuit_Matrix)
    Result = Solve_Linear_Matrix(Y, J, "dc")
    for i in range(len(V)):
        print(f"{V[i]} = {Result[i]}")

elif Circuit_Matrix["analysis"][0]["analysis_type"] == "ac":
########################### AC Analysis ########################### 
    n = Circuit_Matrix["num_nets"] + Circuit_Matrix["vsource_list"].__len__() + Circuit_Matrix["inductor_list"].__len__() + Circuit_Matrix["opamp_list"].__len__()
    from_frequency = Circuit_Matrix["analysis"][0]["freq_start"] * Convert_unit_to_value[Circuit_Matrix["analysis"][0]["freq_start_unit"]]
    to_frequency = Circuit_Matrix["analysis"][0]["freq_stop"] * Convert_unit_to_value[Circuit_Matrix["analysis"][0]["freq_stop_unit"]]
    if from_frequency == 0:
        number_of_decades = int(np.log10(to_frequency/1)) + 1
    else:
        number_of_decades = int(np.log10(to_frequency / from_frequency))
    number_of_frequencies = Circuit_Matrix["analysis"][0]["points_per_dec"]*number_of_decades
    solution_vector = np.zeros([n, number_of_frequencies])
    frequencies = np.linspace(start=from_frequency, stop=to_frequency, num=number_of_frequencies)
    V = []
    for i, frq in enumerate(frequencies):
        Y, V, J = matrix_formulation_AC(Circuit_Matrix, frq)
        solution_vector[:, i, np.newaxis] = Solve_Linear_Matrix(Y, J, "ac")
    Result = Divide_Result_Matrix(solution_vector, V)
    Plot_Output(Circuit_Matrix['plot_name'], frequencies, Result)
# TODO: ADD Opamp to transient 
elif Circuit_Matrix["analysis"][0]["analysis_type"] == "tran":
########################### tran Analysis ###########################

    stop_time = Circuit_Matrix["analysis"][0]["stop_time"]*Convert_unit_to_value[Circuit_Matrix["analysis"][0]["stop_time_unit"]]
    time_step = Circuit_Matrix["analysis"][0]["time_step"]*Convert_unit_to_value[Circuit_Matrix["analysis"][0]["time_step_unit"]]
    steps = np.linspace(start=time_step, stop=stop_time, num=int((stop_time / time_step)))

    ## first step is an op
    n = Circuit_Matrix["num_nets"] + Circuit_Matrix["vsource_list"].__len__() + Circuit_Matrix["inductor_list"].__len__()
    Y, V, J = matrix_formulation_OP(Circuit_Matrix)
    Result = Solve_Linear_Matrix(Y, J, "dc")
    solution_vector = np.zeros([n, len(steps) + 1])
    V = []
    solution_vector[:, 0, np.newaxis] = Result

    solution_vector[1,0] =0 # for step effect

    for i,step in enumerate(steps):
        Y ,V ,J = matrix_formulation_tran(Circuit_Matrix,time_step, old_result = solution_vector[:, i,np.newaxis])
        solution_vector[:, i + 1 , np.newaxis] = Solve_Linear_Matrix(Y, J, "op")

    Result = Divide_Result_Matrix(solution_vector, V)
    # pprint.pprint(solution_vector)
    steps = np.hstack((np.array([0]) , steps))
    Plot_Output(Circuit_Matrix['plot_name'], steps, Result)

