
Convert_unit_to_value = {'G': 1e9,
                         'M': 1e6,
                         'K': 1e3,
                         'm': 1e-3,
                         'u': 1e-6,
                         'n': 1e-9,
                         'p': 1e-12,
                         'nothing': 1
                         }


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


def cap_stamp(Y, elements, sim_type):
    if sim_type == "OP":
        pass
    elif sim_type == "AC":
        pass
    return Y


def ind_stamp(Y, J, num_nets, elements, sim_type):
    if sim_type == "OP":
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
        pass
    else:
        pass


def idc_stamp(J, elements):
    for element in elements:
        from_node = element["from"]
        to_node = element["to"]
        I_value = element["value"] * Convert_unit_to_value[element["unit"]]

        J[from_node] += -I_value
        J[to_node] += I_value
    return J


def vdc_stamp(Y, J, num_nets, elements):
    for i, element in enumerate(elements):
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


def vccs_stamp(Y, num_nets, elements):
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


def vcvs_stamp(Y, num_nets, elements):
    for i, element in enumerate(elements):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        vccs_num = num_nets + i + 1
        A = element["value"] * Convert_unit_to_value[element["unit"]]

        # TODO : construct 'v' vector
        Y[vccs_num][from_node_2] += -A
        Y[vccs_num][to_node_2] += A
        Y[vccs_num][from_node_1] += 1
        Y[vccs_num][to_node_1] += -1

        Y[from_node_1][vccs_num] += 1
        Y[to_node_1][vccs_num] += -1
        Y[from_node_2][vccs_num] += 0
        Y[to_node_2][vccs_num] += 0
    return Y


def cccs_stamp(Y, num_nets, elements):
    for i, element in enumerate(elements):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        cccs_num = num_nets + i + 1
        A = element["value"] * Convert_unit_to_value[element["unit"]]

        # TODO : construct 'v' vector
        Y[cccs_num][from_node_2] += 1
        Y[cccs_num][to_node_2] += -1
        Y[cccs_num][from_node_1] += 0
        Y[cccs_num][to_node_1] += 0

        Y[from_node_1][cccs_num] += A
        Y[to_node_1][cccs_num] += -A
        Y[from_node_2][cccs_num] += 1
        Y[to_node_2][cccs_num] += -1

    return Y


def ccvs_stamp(Y, num_nets, elements):
    for i, element in enumerate(elements):
        from_node_1 = element["from_1"]
        to_node_1 = element["to_1"]
        from_node_2 = element["from_2"]
        to_node_2 = element["to_2"]
        ccvs_num = num_nets + i + 1
        Rm = element["value"] * Convert_unit_to_value[element["unit"]]

        # TODO : construct 'v' vector
        Y[ccvs_num][from_node_2] += 1
        Y[ccvs_num][to_node_2] += -1
        Y[ccvs_num][from_node_1] += 0
        Y[ccvs_num][to_node_1] += 0

        Y[from_node_1][ccvs_num] += 0
        Y[to_node_1][ccvs_num] += 0
        Y[from_node_2][ccvs_num] += 1
        Y[to_node_2][ccvs_num] += -1

        Y[ccvs_num+1][from_node_2] += 0
        Y[ccvs_num+1][to_node_2] += 0
        Y[ccvs_num+1][from_node_1] += 1
        Y[ccvs_num+1][to_node_1] += -1
        Y[ccvs_num+1][ccvs_num] += -Rm

        Y[from_node_1][ccvs_num+1] += 1
        Y[to_node_1][ccvs_num+1] += -1
        Y[from_node_2][ccvs_num+1] += 0
        Y[to_node_2][ccvs_num+1] += 0

    return Y
