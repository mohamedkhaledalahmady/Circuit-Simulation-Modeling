import numpy as np

Convert_unit_to_value = {'g': 1e9, 'M': 1e6, 'K': 1e3,'nothing':1, 'm': 1e-3, 'u': 1e-6, 'n': 1e-9, 'p': 1e-12}

def res_stamp(Y, elements):
    for element in elements:
        from_node = element["from"]
        to_node = element["to"]
        res_value = element["value"] * Convert_unit_to_value[element["unit"]]

        Y[from_node][from_node] += 1 / res_value
        Y[to_node][to_node] += 1 / res_value
        Y[from_node][to_node] += -1 / res_value
        Y[to_node][from_node] += -1 / res_value
    return Y

def cap_stamp(Y, elements,sim_type,W):
    if sim_type == "OP":
        pass
    elif sim_type == "AC":
        pass
    return Y


def ind_stamp(Y,J,num_nets, elements,sim_type):
    if sim_type == "OP":
        for i, element in enumerate(elements):
            from_node = element["from"]
            to_node = element["to"]
            ind_num = num_nets + i + 1

            # TODO : constract 'v' vector
            Y[from_node][ind_num] = -1
            Y[to_node][ind_num] = 1
            Y[ind_num][to_node] = 1
            Y[ind_num][from_node] = -1
            J[ind_num] = 0
        pass
    else:
        pass

def idc_stamp(J, elements):
    for element in elements:
        from_node = element["from"]
        to_node = element["to"]
        I_value = element["value"] * Convert_unit_to_value[element["unit"]]

        J[from_node] = -I_value
        J[to_node] = I_value
    return J

def vdc_stamp(Y, J,num_nets, elements):
    for i,element in enumerate(elements):
        from_node = element["from"]
        to_node = element["to"]
        vdc_num = num_nets + i + 1
        v_value = element["value"] * Convert_unit_to_value[element["unit"]]

        # TODO : constract 'v' vector
        Y[from_node][vdc_num] = -1
        Y[to_node][vdc_num] = 1
        Y[vdc_num][to_node] = 1
        Y[vdc_num][from_node] = -1

        J[vdc_num] += v_value

    return Y,J

