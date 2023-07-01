import numpy as np
import Element_stamps

def matrix_formulation_OP(elements):
    n = elements["num_nets"] + elements["vsource_list"].__len__() + elements["inductor_list"].__len__() + elements["vcvs_list"].__len__() \
    + elements["cccs_list"].__len__() + 2*elements["ccvs_list"].__len__()
    print(n)
    Y = np.zeros([n+1,n+1])
    J = np.zeros([n+1,1])
    simulation = { "type" : "op",
                   "num_nets_for_ind" : elements["num_nets"] + elements["vsource_list"].__len__(),
                   "num_nets_for_vsource": elements["num_nets"],
                   "num_nets_for_vcvs" : elements["num_nets"] + elements["vsource_list"].__len__() + elements["vsource_list"].__len__(),
                   "num_nets_for_cccs" : elements["num_nets"] + elements["vsource_list"].__len__() + elements["vsource_list"].__len__() +\
                    elements["vcvs_list"].__len__(),
                   "num_nets_for_ccvs" : elements["num_nets"] + elements["vsource_list"].__len__() + elements["vsource_list"].__len__() +\
                    elements["vcvs_list"].__len__() + elements["cccs_list"].__len__(),
    }
    # TODO : is this calling by ref ?! , so why return in stamp functions
    Element_stamps.res_stamp(Y,elements["resistor_list"])
    Element_stamps.cap_stamp(Y,elements["capacitor_list"],simulation)
    Element_stamps.idc_stamp(J,elements["isource_list"],simulation)
    Element_stamps.ind_stamp(Y,J,elements["inductor_list"],simulation)
    Element_stamps.vdc_stamp(Y,J,elements["vsource_list"],simulation)
    Element_stamps.vccs_stamp(Y,elements["vccs_list"],simulation)
    Element_stamps.vcvs_stamp(Y,elements["vcvs_list"],simulation)
    Element_stamps.cccs_stamp(Y,elements["cccs_list"],simulation)
    Element_stamps.ccvs_stamp(Y, elements["ccvs_list"],simulation)

    return Y, J

def matrix_formulation_AC(elements,freq):
    n = elements["num_nets"] + elements["vsource_list"].__len__()

    Y = np.zeros([n+1,n+1],dtype = "complex")
    J = np.zeros([n+1,1])
    # TODO : is this calling by ref ?! , so why return in stamp functions
    simulation = { "type" : "ac",
                   "freq" : freq,
                   "num_nets_for_ind" : elements["num_nets"],
                   "num_nets_for_vsource": elements["num_nets"]
    }
    Element_stamps.res_stamp(Y,elements["resistor_list"])
    Element_stamps.cap_stamp(Y,elements["capacitor_list"],simulation)
    Element_stamps.idc_stamp(J,elements["isource_list"],simulation)
    Element_stamps.ind_stamp(Y,J,elements["inductor_list"],simulation)
    Element_stamps.vdc_stamp(Y,J,elements["vsource_list"],simulation)
    Element_stamps.vccs_stamp(Y,elements["vccs_list"],simulation)


    return Y, J
