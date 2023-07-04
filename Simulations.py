import numpy as np
import Element_stamps
from typing import List, Dict
import matplotlib.pyplot as plt


def matrix_formulation_OP(elements):
    n = elements["num_nets"] + elements["vsource_list"].__len__() + elements["inductor_list"].__len__() + elements["vcvs_list"].__len__() \
        + elements["cccs_list"].__len__() + 2*elements["ccvs_list"].__len__()
    Y = np.zeros([n+1, n+1])
    J = np.zeros([n+1, 1])
    V = []
    # Construct Unknown Vector 'V'
    for i in range(elements["num_nets"]):
        V.append(f"V{i+1}")
    simulation = {
        "type": "op",
        "num_nets_for_vsource": elements["num_nets"],
        "num_nets_for_ind": elements["num_nets"] + elements["vsource_list"].__len__(),
        "num_nets_for_vcvs": elements["num_nets"] + elements["vsource_list"].__len__() + elements["inductor_list"].__len__(),
        "num_nets_for_cccs": elements["num_nets"] + elements["vsource_list"].__len__() + elements["inductor_list"].__len__() +
        elements["vcvs_list"].__len__(),
        "num_nets_for_ccvs": elements["num_nets"] + elements["vsource_list"].__len__() + elements["inductor_list"].__len__() +
        elements["vcvs_list"].__len__(
        ) + elements["cccs_list"].__len__(),
    }

    # TODO : is this calling by ref ?! , so why return in stamp functions
    Element_stamps.res_stamp(Y, elements["resistor_list"])
    Element_stamps.cap_stamp(Y, elements["capacitor_list"], simulation)
    Element_stamps.idc_stamp(J, elements["isource_list"], simulation)
    Element_stamps.vdc_stamp(Y, V, J, elements["vsource_list"], simulation)
    Element_stamps.ind_stamp(Y, V, J, elements["inductor_list"], simulation)
    Element_stamps.vccs_stamp(Y, elements["vccs_list"], simulation)
    Element_stamps.vcvs_stamp(Y, V, elements["vcvs_list"], simulation)
    Element_stamps.cccs_stamp(Y, V, elements["cccs_list"], simulation)
    Element_stamps.ccvs_stamp(Y, V, elements["ccvs_list"], simulation)

    return Y, V, J


def matrix_formulation_AC(elements, freq):
    n = elements["num_nets"] + elements["vsource_list"].__len__() + elements["inductor_list"].__len__()
    Y = np.zeros([n+1, n+1], dtype="complex")
    J = np.zeros([n+1, 1])
    V = []
    # Construct Unknown Vector 'V'
    for i in range(elements["num_nets"]):
        V.append(f"V{i+1}")
    # TODO : is this calling by ref ?! , so why return in stamp functions
    simulation = {
        "type": "ac",
        "freq": freq,
        "num_nets_for_vsource": elements["num_nets"],
        "num_nets_for_ind": elements["num_nets"] + elements["vsource_list"].__len__()
    }

    Y = Element_stamps.res_stamp(Y, elements["resistor_list"])
    Y = Element_stamps.cap_stamp(Y, elements["capacitor_list"], simulation)
    J = Element_stamps.idc_stamp(J, elements["isource_list"], simulation)
    Y, V, J = Element_stamps.vdc_stamp(Y, V, J, elements["vsource_list"], simulation)
    Y, V, J = Element_stamps.ind_stamp(Y, V, J, elements["inductor_list"], simulation)
    Y = Element_stamps.vccs_stamp(Y, elements["vccs_list"], simulation)

    return Y, V, J

def Divide_Result_Matrix(Solution_Matrix: np.array, V: List) -> Dict:
    Result_Dict = {}
    for i in range(len(V)):
        Result_Dict[V[i]] = Solution_Matrix[i, :]
    return Result_Dict
    

def Plot_Output(Plot_name, frequencies, Result):
    plt.plot(frequencies, Result[Plot_name], 'r')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title(f"{Plot_name} Curve")
    plt.xscale('log')
    plt.grid(True)
    plt.show()