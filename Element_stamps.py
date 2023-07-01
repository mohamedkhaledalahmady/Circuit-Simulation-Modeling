from typing import Dict,List
import numpy as np
Convert_unit_to_value = {'G': 1e9,
                         'M': 1e6,
                         'K': 1e3,
                         'm': 1e-3,
                         'u': 1e-6,
                         'n': 1e-9,
                         'p': 1e-12,
                         'nothing': 1
                         }

def res_stamp(Y : np.array , elements : List[Dict]):
    for element in elements:
        from_node = element["from"]
        to_node = element["to"]
        res_value = element["value"] * Convert_unit_to_value[element["unit"]]

        Y[from_node][from_node] += 1 / res_value
        Y[to_node][to_node] += 1 / res_value
        Y[from_node][to_node] += -1 / res_value
        Y[to_node][from_node] += -1 / res_value
    return Y

def cap_stamp(Y : np.array , elements : List[Dict], simulatation : Dict):
    if simulatation["type"] == "op":
        pass
    elif simulatation["type"] == "ac":
        W = simulatation["freq"]
        for element in elements:
            from_node = element["from"]
            to_node = element["to"]
            cap_value = element["value"] * Convert_unit_to_value[element["unit"]]
            Y[from_node][from_node] += 1j*W*cap_value
            Y[to_node][to_node] += 1j*W*cap_value
            Y[from_node][to_node] += -1j*W*cap_value
            Y[to_node][from_node] += -1j*W*cap_value
    return Y

def ind_stamp(Y : np.array,J : np.array , elements : List[Dict], simulatation : Dict):

    if simulatation["type"] == "OP":
        num_nets = simulatation["num_nets_for_ind"]
        for i, element in enumerate(elements):
            from_node = element["from"]
            to_node = element["to"]
            ind_num = num_nets + i + 1

            # TODO : construct 'v' vector
            Y[from_node][ind_num] = 1
            Y[to_node][ind_num] = -1
            Y[ind_num][to_node] = -1
            Y[ind_num][from_node] = 1
            J[ind_num] = 0

    elif simulatation["type"] == "AC":
        W = simulatation["freq"]
        for element in elements:
            from_node = element["from"]
            to_node = element["to"]
            ind_value = element["value"] * Convert_unit_to_value[element["unit"]]

            Y[from_node][from_node] += 1/ (1j * W * ind_value)
            Y[to_node][to_node] += 1/ (1j * W * ind_value)
            Y[from_node][to_node] += -1/ (1j * W * ind_value)
            Y[to_node][from_node] += -1 / (1j * W * ind_value)
    return Y,J

def idc_stamp(J : np.array , elements : List[Dict], simulatation : Dict):

    for element in elements:
        if element["type"] == "dc" and simulatation["type"] == "op":
            from_node = element["from"]
            to_node = element["to"]
            I_value = element["value"] * Convert_unit_to_value[element["unit"]]

            J[from_node] = -I_value
            J[to_node] = I_value
        else:
            if element["type"] == "ac" and simulatation["type"] == "ac":
                from_node = element["from"]
                to_node = element["to"]
                I_value = element["value"] * Convert_unit_to_value[element["unit"]]

                J[from_node] = -I_value
                J[to_node] = I_value
    return J

def vdc_stamp(Y : np.array,J : np.array , elements : List[Dict], simulatation : Dict):

    for i, element in enumerate(elements):
        num_nets = simulatation["num_nets_for_vsource"]
        if element["type"] == "dc" and simulatation["type"] == "op":
            from_node = element["from"]
            to_node = element["to"]
            vdc_num = num_nets + i + 1
            v_value = element["value"] * Convert_unit_to_value[element["unit"]]

            # TODO : construct 'v' vector
            Y[from_node][vdc_num] = 1
            Y[to_node][vdc_num] = -1
            Y[vdc_num][to_node] = -1
            Y[vdc_num][from_node] = 1

            J[vdc_num] += v_value
        else:
            if element["type"] == "ac" and simulatation["type"] == "ac":
                from_node = element["from"]
                to_node = element["to"]
                vdc_num = num_nets + i + 1
                v_value = element["value"] * Convert_unit_to_value[element["unit"]]

                # TODO : construct 'v' vector
                Y[from_node][vdc_num] = 1
                Y[to_node][vdc_num] = -1
                Y[vdc_num][to_node] = -1
                Y[vdc_num][from_node] = 1

                J[vdc_num] += v_value
    return Y, J

def vccs_stamp(Y : np.array, elements : List[Dict], simulatation : Dict):
    # todo : to be updated
    for i, element in enumerate(elements):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        gm = element["value"] * Convert_unit_to_value[element["unit"]]

        # TODO : construct 'v' vector
        Y[from_node_1][from_node_2] = gm
        Y[to_node_1][to_node_2] = gm
        Y[from_node_1][to_node_2] = -gm
        Y[to_node_1][from_node_2] = -gm

    return Y
