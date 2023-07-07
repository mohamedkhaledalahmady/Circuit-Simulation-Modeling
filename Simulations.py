import numpy as np
import Element_stamps
from typing import List, Dict
import matplotlib.pyplot as plt

Convert_unit_to_value = {'G': 1e9,
                         'M': 1e6,
                         'K': 1e3,
                         'm': 1e-3,
                         'u': 1e-6,
                         'n': 1e-9,
                         'p': 1e-12,
                         "f": 1e-15,
                         'nothing': 1
                         }

def matrix_formulation_OP(elements):
    n = elements["num_nets"] + elements["vsource_list"].__len__() + elements["inductor_list"].__len__() + elements["vcvs_list"].__len__() \
        + elements["cccs_list"].__len__() + 2*elements["ccvs_list"].__len__() + elements["opamp_list"].__len__()
    Y = np.zeros([n+1, n+1])
    J = np.zeros([n+1, 1])
    V = []
    # Construct Unknown Vector 'V'
    for i in range(elements["num_nets"]):
        V.append(f"V{i+1}")


    for element in elements["resistor_list"]:
        from_node = element["from"]
        to_node = element["to"]
        value = element["value"] * Convert_unit_to_value[element["unit"]]
        Element_stamps.res_stamp(Y, from_node = from_node , to_node= to_node , res_value= value)

    for element in elements["isource_list"]:
        from_node = element["from"]
        to_node = element["to"]
        value = element["value"] * Convert_unit_to_value[element["unit"]]
        Element_stamps.idc_stamp(J, from_node = from_node , to_node= to_node , I_value= value)

    for element in elements["capacitor_list"]:
        # o.c is an Isource with I = 0
        from_node = element["from"]
        to_node = element["to"]
        value = 0
        Element_stamps.idc_stamp(J, from_node = from_node , to_node= to_node , I_value= value)

    position =  elements["num_nets"]
    for i, element in enumerate(elements["vsource_list"]):
        from_node = element["from"]
        to_node = element["to"]
        vdc_num = position + i + 1
        v_value = element["value"] * Convert_unit_to_value[element["unit"]]
        V.append("I_" + element["instance_name"])
        Element_stamps.vdc_stamp(Y, J, from_node = from_node , to_node= to_node , v_value= v_value , vdc_num = vdc_num)

    position += elements["vsource_list"].__len__()
    for i, element in enumerate(elements["inductor_list"]):
        # s.c is a Vsource with E = 0
        from_node = element["from"]
        to_node = element["to"]
        ind_num = position + i + 1
        V.append("I_" + element["instance_name"])
        Element_stamps.vdc_stamp(Y, J, from_node = from_node , to_node= to_node , v_value= 0 , vdc_num = ind_num)

    
    for i, element in enumerate(elements["vccs_list"]):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        gm = element["value"] * Convert_unit_to_value[element["unit"]]
        Element_stamps.vccs_stamp(Y, from_nodes = (from_node_1,from_node_2) , to_nodes= (to_node_1,to_node_2) , gm= gm)

    position += elements["inductor_list"].__len__()
    for i, element in enumerate(elements["vcvs_list"]):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        vcvs_num = position + i + 1
        A = element["value"] * Convert_unit_to_value[element["unit"]]
        V.append("I_" + element["instance_name"])
        Element_stamps.vcvs_stamp(Y, from_nodes = (from_node_1,from_node_2) , to_nodes= (to_node_1,to_node_2) , A=A, vcvs_num = vcvs_num)

    position += elements["vcvs_list"].__len__()
    for i, element in enumerate(elements["cccs_list"]):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        cccs_num = position + i + 1
        A = element["value"] * Convert_unit_to_value[element["unit"]]
        V.append("I_" + element["instance_name"])

        Element_stamps.cccs_stamp(Y, from_nodes = (from_node_1,from_node_2) , to_nodes= (to_node_1,to_node_2) , A=A, cccs_num = cccs_num)

    position += elements["cccs_list"].__len__()
    for i, element in enumerate(elements["ccvs_list"]):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        ccvs_num = position + i + 1
        Rm = element["value"] * Convert_unit_to_value[element["unit"]]

        V.append("I_" + element["instance_name"] + "_1")
        V.append("I_" + element["instance_name"] + "_2")
        Element_stamps.ccvs_stamp(Y, from_nodes = (from_node_1,from_node_2) , to_nodes= (to_node_1,to_node_2) , Rm=Rm, ccvs_num = ccvs_num)


    position += elements["ccvs_list"].__len__()
    for i, element in enumerate(elements["opamp_list"]):
        neg_terminal = element["neg_terminal"]
        pos_terminal = element["pos_terminal"]
        out_terminal = element["out_terminal"]
        opamp_num = position + i + 1

        V.append("I_" + element["instance_name"])
        Element_stamps.opamp_stamp(Y, neg_terminal = neg_terminal , pos_terminal = pos_terminal , out_terminal = out_terminal, opamp_num = opamp_num)

    return Y, V, J

def matrix_formulation_AC(elements, freq):
    n = elements["num_nets"] + elements["vsource_list"].__len__() +elements["inductor_list"].__len__()+ elements["vcvs_list"].__len__() \
        + elements["cccs_list"].__len__() + 2*elements["ccvs_list"].__len__() + elements["opamp_list"].__len__()
    Y = np.zeros([n+1, n+1], dtype="complex")
    J = np.zeros([n+1, 1])
    V = []
    # Construct Unknown Vector 'V'
    for i in range(elements["num_nets"]):
        V.append(f"V{i+1}")

    for element in elements["resistor_list"]:
        from_node = element["from"]
        to_node = element["to"]
        value = element["value"] * Convert_unit_to_value[element["unit"]]
        Element_stamps.res_stamp(Y, from_node = from_node , to_node= to_node , res_value= value)

    for element in elements["isource_list"]:
        from_node = element["from"]
        to_node = element["to"]
        value = element["value"] * Convert_unit_to_value[element["unit"]]
        Element_stamps.idc_stamp(J, from_node = from_node , to_node= to_node , I_value= value)

    for element in elements["capacitor_list"]:
        # the cap is a gm = jwc
        from_node = element["from"]
        to_node = element["to"]
        if freq == 0:
            pass
        else:
            value = 1/(1j*2*np.pi*freq*element["value"] * Convert_unit_to_value[element["unit"]])
            Element_stamps.res_stamp(Y, from_node = from_node , to_node= to_node , res_value= value)

    position = elements["num_nets"]
    for i, element in enumerate(elements["vsource_list"]):
        from_node = element["from"]
        to_node = element["to"]
        vdc_num = position + i + 1
        v_value = element["value"] * Convert_unit_to_value[element["unit"]]
        V.append("I_" + element["instance_name"])
        Element_stamps.vdc_stamp(Y, J, from_node = from_node , to_node= to_node , v_value= v_value , vdc_num = vdc_num)

    position += elements["vsource_list"].__len__()
    for i, element in enumerate(elements["inductor_list"]):
        # the ind is a res = jwL
        from_node = element["from"]
        to_node = element["to"]
        ind_num = position + i + 1
        V.append("I_" + element["instance_name"])
        Element_stamps.vdc_stamp(Y, J, from_node=from_node, to_node=to_node, v_value=0, vdc_num=ind_num) 
        if freq == 0:
            value = np.inf
        else:
            value = 1/(1j*freq*2*np.pi*element["value"] * Convert_unit_to_value[element["unit"]])
        Element_stamps.res_stamp(Y, from_node = 0 , to_node= ind_num , res_value= -value)

    for i, element in enumerate(elements["vccs_list"]):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        gm = element["value"] * Convert_unit_to_value[element["unit"]]
        Element_stamps.vccs_stamp(Y, from_nodes = (from_node_1,from_node_2) , to_nodes= (to_node_1,to_node_2) , gm= gm)

    for i, element in enumerate(elements["vcvs_list"]):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        vcvs_num = position + i + 1
        A = element["value"] * Convert_unit_to_value[element["unit"]]

        V.append("I_" + element["instance_name"])
        Element_stamps.vcvs_stamp(Y, from_nodes = (from_node_1,from_node_2) , to_nodes= (to_node_1,to_node_2) , A=A, vcvs_num = vcvs_num)

    position += elements["vcvs_list"].__len__()
    for i, element in enumerate(elements["cccs_list"]):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        cccs_num = position + i + 1
        A = element["value"] * Convert_unit_to_value[element["unit"]]
        V.append("I_" + element["instance_name"])

        Element_stamps.cccs_stamp(Y, from_nodes = (from_node_1,from_node_2) , to_nodes= (to_node_1,to_node_2) , A=A, cccs_num = cccs_num)

    position += elements["cccs_list"].__len__()
    for i, element in enumerate(elements["ccvs_list"]):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        ccvs_num = position + i + 1
        Rm = element["value"] * Convert_unit_to_value[element["unit"]]

        V.append("I_" + element["instance_name"] + "_1")
        V.append("I_" + element["instance_name"] + "_2")
        Element_stamps.ccvs_stamp(Y, from_nodes = (from_node_1,from_node_2) , to_nodes= (to_node_1,to_node_2) , Rm=Rm, ccvs_num = ccvs_num)

    position += elements["ccvs_list"].__len__()
    for i, element in enumerate(elements["opamp_list"]):
        neg_terminal = element["neg_terminal"]
        pos_terminal = element["pos_terminal"]
        out_terminal = element["out_terminal"]
        opamp_num = position + i + 1

        V.append("I_" + element["instance_name"])
        Element_stamps.opamp_stamp(Y, neg_terminal = neg_terminal , pos_terminal = pos_terminal , out_terminal = out_terminal, opamp_num = opamp_num)

    return Y, V, J

def matrix_formulation_tran(elements, time_step , old_result):
    n = elements["num_nets"] + elements["vsource_list"].__len__() + + elements["vcvs_list"].__len__() \
        + elements["cccs_list"].__len__() + 2 * elements["ccvs_list"].__len__()
    Y = np.zeros([n + 1, n + 1])
    J = np.zeros([n + 1, 1])
    V = []
    # Construct Unknown Vector 'V'
    for i in range(elements["num_nets"]):
        V.append(f"V{i + 1}")

    for element in elements["resistor_list"]:
        from_node = element["from"]
        to_node = element["to"]
        value = element["value"] * Convert_unit_to_value[element["unit"]]
        Element_stamps.res_stamp(Y, from_node=from_node, to_node=to_node, res_value=value)

    for element in elements["isource_list"]:
        from_node = element["from"]
        to_node = element["to"]
        value = element["value"] * Convert_unit_to_value[element["unit"]]
        Element_stamps.idc_stamp(J, from_node=from_node, to_node=to_node, I_value=value)

    for element in elements["capacitor_list"]:
        from_node = element["from"]
        to_node = element["to"]
        cap_value = (element["value"] * Convert_unit_to_value[element["unit"]])
        res_value = time_step/ cap_value
        Element_stamps.res_stamp(Y, from_node=from_node, to_node=to_node, res_value=res_value)

        results = np.vstack((np.array([0]), old_result))
        previous_volt_drop = float(results[to_node] - results[from_node])

        I_value = cap_value * previous_volt_drop / time_step
        Element_stamps.idc_stamp(J, from_node=from_node, to_node=to_node, I_value=I_value)

    position = elements["num_nets"]
    for i, element in enumerate(elements["vsource_list"]):
        from_node = element["from"]
        to_node = element["to"]
        vdc_num = position + i + 1
        v_value = element["value"] * Convert_unit_to_value[element["unit"]]
        V.append("I_" + element["instance_name"])
        Element_stamps.vdc_stamp(Y, J, from_node=from_node, to_node=to_node, v_value=v_value, vdc_num=vdc_num)

    position += elements["vsource_list"].__len__()
    for i, element in enumerate(elements["inductor_list"]):
        pass

    for i, element in enumerate(elements["vccs_list"]):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        gm = element["value"] * Convert_unit_to_value[element["unit"]]
        Element_stamps.vccs_stamp(Y, from_nodes=(from_node_1, from_node_2), to_nodes=(to_node_1, to_node_2), gm=gm)

    for i, element in enumerate(elements["vcvs_list"]):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        vcvs_num = position + i + 1
        A = element["value"] * Convert_unit_to_value[element["unit"]]

        V.append("I_" + element["instance_name"])
        Element_stamps.vcvs_stamp(Y, from_nodes=(from_node_1, from_node_2), to_nodes=(to_node_1, to_node_2), A=A,
                                  vcvs_num=vcvs_num)

    position += elements["vcvs_list"].__len__()
    for i, element in enumerate(elements["cccs_list"]):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        cccs_num = position + i + 1
        A = element["value"] * Convert_unit_to_value[element["unit"]]
        V.append("I_" + element["instance_name"])

        Element_stamps.cccs_stamp(Y, from_nodes=(from_node_1, from_node_2), to_nodes=(to_node_1, to_node_2), A=A,
                                  cccs_num=cccs_num)

    position += elements["cccs_list"].__len__()
    for i, element in enumerate(elements["ccvs_list"]):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        ccvs_num = position + i + 1
        Rm = element["value"] * Convert_unit_to_value[element["unit"]]

        V.append("I_" + element["instance_name"] + "_1")
        V.append("I_" + element["instance_name"] + "_2")
        Element_stamps.ccvs_stamp(Y, from_nodes=(from_node_1, from_node_2), to_nodes=(to_node_1, to_node_2), Rm=Rm,
                                  ccvs_num=ccvs_num)

    return Y, V, J

def Divide_Result_Matrix(Solution_Matrix: np.array, V: List) -> Dict:
    Result_Dict = {}
    for i in range(len(V)):
        Result_Dict[V[i]] = Solution_Matrix[i, :]
    return Result_Dict

def Plot_Output(Plot_name, frequencies, Result):
    for i, val in enumerate(Plot_name):
        plt.figure()
        # plt.plot(frequencies, 20*np.log10(Result[val]), 'r')
        plt.plot(frequencies, Result[val], 'r')
        # plt.xlabel('Frequency (Hz)')
        plt.xlabel('Time (sec)')
        plt.ylabel('Amplitude')
        plt.title(f"{val} Curve")
        # plt.xscale('log')
        plt.grid(True)
    plt.show()