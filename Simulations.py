import numpy as np
import Element_stamps

def matrix_formulation(elements):
    n = elements["num_nets"] + elements["vsource_list"].__len__() + elements["inductor_list"].__len__()
    Y = np.zeros([n+1,n+1])
    J = np.zeros([n+1,1])
    Element_stamps.res_stamp(Y,elements["resistor_list"])
    Element_stamps.cap_stamp(Y,elements["capacitor_list"],"OP")
    Element_stamps.idc_stamp(J,elements["isource_list"])
    Element_stamps.ind_stamp(Y,J,elements["num_nets"],elements["inductor_list"],"OP")
    Element_stamps.vdc_stamp(Y,J,elements["num_nets"] + elements["inductor_list"].__len__(),elements["vsource_list"])

    return Y, J

