from typing import List, Dict
from Regular_Expressions import *


def Resistor_Parsing(resistor_line: str) -> Dict:
    """
    This Function parse resistor_line to its parameters into dictionary as follow
    dict={"instance_name", "component_type", "from", "to", "type", "value", "unit"}
    """
    resistor_line_split = resistor_line.split()
    dict = {
        "instance_name": resistor_line_split[0],
        "component_type": resistor_line_split[1],
        "from": int(resistor_line_split[2]),
        "to": int(resistor_line_split[3]),
        "value": int(resistor_line_split[4][:-1]) if not resistor_line_split[4][-1].isdigit() else int(resistor_line_split[4]),
        "unit": resistor_line_split[4][-1] if not resistor_line_split[4][-1].isdigit() else "nothing"
    }
    return dict


def Capacitor_Parsing(capacitor_line: str) -> Dict:
    """
    This Function parse capacitor_line to its parameters into dictionary as follow
    dict={"instance_name", "component_type", "from", "to", "type", "value", "unit"}
    """
    capacitor_line_split = capacitor_line.split()
    dict = {
        "instance_name": capacitor_line_split[0],
        "component_type": capacitor_line_split[1],
        "from": int(capacitor_line_split[2]),
        "to": int(capacitor_line_split[3]),
        "value": int(capacitor_line_split[4][:-1]) if not capacitor_line_split[4][-1].isdigit() else int(capacitor_line_split[4]),
        "unit": capacitor_line_split[4][-1] if not capacitor_line_split[4][-1].isdigit() else "nothing"
    }
    return dict


def Inductor_Parsing(inductor_line: str) -> Dict:
    """
    This Function parse inductor_line to its parameters into dictionary as follow
    dict={"instance_name", "component_type", "from", "to", "type", "value", "unit"}
    """
    inductor_line_split = inductor_line.split()
    dict = {
        "instance_name": inductor_line_split[0],
        "component_type": inductor_line_split[1],
        "from": int(inductor_line_split[2]),
        "to": int(inductor_line_split[3]),
        "value": int(inductor_line_split[4][:-1]) if not inductor_line_split[4][-1].isdigit() else int(inductor_line_split[4]),
        "unit": inductor_line_split[4][-1] if not inductor_line_split[4][-1].isdigit() else "nothing"
    }
    return dict


def Voltage_dc_Parsing(voltage_dc_line: str) -> Dict:
    """
    This Function parse voltage_dc_line to its parameters into dictionary as follows
    dict={"instance_name", "component_type", "from", "to", "type", "value", "unit"}
    """
    voltage_dc_line_split = voltage_dc_line.split()
    dict = {
        "instance_name": voltage_dc_line_split[0],
        "component_type": voltage_dc_line_split[1],
        "from": int(voltage_dc_line_split[2]),
        "to": int(voltage_dc_line_split[3]),
        "type": voltage_dc_line_split[4],
        # TODO : the type must be lower case or change from stamp
        "value": int(voltage_dc_line_split[5][:-1]) if not voltage_dc_line_split[5][-1].isdigit() else int(voltage_dc_line_split[5]),
        "unit": voltage_dc_line_split[5][-1] if not voltage_dc_line_split[5][-1].isdigit() else "nothing"
    }
    return dict


def Current_dc_Parsing(current_dc_line: str) -> Dict:
    """
    This Function parse current_dc_line to its parameters into dictionary as follow
    dict={"instance_name", "component_type", "from", "to", "type", "value", "unit"}
    """
    current_dc_line_split = current_dc_line.split()
    dict = {
        "instance_name": current_dc_line_split[0],
        "component_type": current_dc_line_split[1],
        "from": int(current_dc_line_split[2]),
        "to": int(current_dc_line_split[3]),
        # TODO : the type must be lower case or change from stamp
        "type": current_dc_line_split[4],
        "value": int(current_dc_line_split[5][:-1]) if not current_dc_line_split[5][-1].isdigit() else int(current_dc_line_split[5]),
        "unit": current_dc_line_split[5][-1] if not current_dc_line_split[5][-1].isdigit() else "nothing"
    }
    return dict


def VCCS_Parsing(vccs_line: str) -> Dict:
    """
    This Function parse vccs_line to its parameters into dictionary as follow
    dict={"instance_name", "component_type", "from_1", "to_1", "from_2", "to_2", "type", "value", "unit"}
    """
    vccs_line_split = vccs_line.split()
    dict = {
        "instance_name": vccs_line_split[0],
        "component_type": vccs_line_split[1],
        "from_1": int(vccs_line_split[2]),
        "to_1": int(vccs_line_split[3]),
        "from_2": int(vccs_line_split[4]),
        "to_2": int(vccs_line_split[5]),
        # TODO : the type must be lower case or change from stamp
        "type": vccs_line_split[6],
        "value": int(vccs_line_split[7][:-1]) if not vccs_line_split[7][-1].isdigit() else int(vccs_line_split[7]),
        "unit": vccs_line_split[7][-1] if not vccs_line_split[7][-1].isdigit() else "nothing"
    }
    return dict


def VCVS_Parsing(vcvs_line: str) -> Dict:
    """
    This Function parse vcvs_line to its parameters into dictionary as follow
    dict={"instance_name", "component_type", "from_1", "to_1", "from_2", "to_2", "type", "value", "unit"}
    """
    vcvs_line_split = vcvs_line.split()
    dict = {
        "instance_name": vcvs_line_split[0],
        "component_type": vcvs_line_split[1],
        "from_1": int(vcvs_line_split[2]),
        "to_1": int(vcvs_line_split[3]),
        "from_2": int(vcvs_line_split[4]),
        "to_2": int(vcvs_line_split[5]),
        "type": vcvs_line_split[6],
        "value": int(vcvs_line_split[7][:-1]) if not vcvs_line_split[7][-1].isdigit() else int(vcvs_line_split[7]),
        "unit": vcvs_line_split[7][-1] if not vcvs_line_split[7][-1].isdigit() else "nothing"
    }
    return dict


def CCCS_Parsing(cccs_line: str) -> Dict:
    """
    This Function parse cccs_line to its parameters into dictionary as follow
    dict={"instance_name", "component_type", "from_1", "to_1", "from_2", "to_2", "type", "value", "unit"}
    """
    cccs_line_split = cccs_line.split()
    dict = {
        "instance_name": cccs_line_split[0],
        "component_type": cccs_line_split[1],
        "from_1": int(cccs_line_split[2]),
        "to_1": int(cccs_line_split[3]),
        "from_2": int(cccs_line_split[4]),
        "to_2": int(cccs_line_split[5]),
        "type": cccs_line_split[6],
        "value": int(cccs_line_split[7][:-1]) if not cccs_line_split[7][-1].isdigit() else int(cccs_line_split[7]),
        "unit": cccs_line_split[7][-1] if not cccs_line_split[7][-1].isdigit() else "nothing"
    }
    return dict

def CCVS_Parsing(ccvs_line: str) -> Dict:
    """
    This Function parse ccvs_line to its parameters into dictionary as follow
    dict={"instance_name", "component_type", "from_1", "to_1", "from_2", "to_2", "type", "value", "unit"}
    """
    ccvs_line_split = ccvs_line.split()
    dict = {
        "instance_name": ccvs_line_split[0],
        "component_type": ccvs_line_split[1],
        "from_1": int(ccvs_line_split[2]),
        "to_1": int(ccvs_line_split[3]),
        "from_2": int(ccvs_line_split[4]),
        "to_2": int(ccvs_line_split[5]),
        "type": ccvs_line_split[6],
        "value": int(ccvs_line_split[7][:-1]) if not ccvs_line_split[7][-1].isdigit() else int(ccvs_line_split[7]),
        "unit": ccvs_line_split[7][-1] if not ccvs_line_split[7][-1].isdigit() else "nothing"
    }
    return dict


def Get_Number_of_Nets(circuit_dict: dict) -> int:
    """
    This Function determine and return the number of nets in the circuit
    """
    number_of_nets = 0
    for i, val in enumerate(circuit_dict):
        if circuit_dict[val] != [] and circuit_dict[val] != int:
            for j, v in enumerate(circuit_dict[val]):
                number_of_nets = max(
                    number_of_nets, circuit_dict["resistor_list"][j]['from'], circuit_dict["resistor_list"][j]['to'])
        else:
            pass
    return number_of_nets


def parser(content: str) -> Dict:
    content_without_dashed_lines = []
    circuit_dict = {"num_nets": int,
                    "resistor_list": [],
                    "vsource_list": [],
                    "isource_list": [],
                    "capacitor_list": [],
                    "inductor_list": [],
                    "vccs_list": [],
                    "vcvs_list": [],
                    "cccs_list": [],
                    "ccvs_list": []
                    }
    for i, val in enumerate(content):
        if '//' not in val:
            val = val+' ' if i != len(content)-1 else val
            content_without_dashed_lines.append(val)

    for i, val in enumerate(content_without_dashed_lines):
        if Resistor_Regx(val):
            circuit_dict["resistor_list"].append(Resistor_Parsing(val))
        elif Capacitor_Regx(val):
            circuit_dict["capacitor_list"].append(Capacitor_Parsing(val))
        elif Inductor_Regx(val):
            circuit_dict["inductor_list"].append(Inductor_Parsing(val))
        elif Voltage_DC_Regx(val):
            circuit_dict["vsource_list"].append(Voltage_dc_Parsing(val))
        elif Current_DC_Regx(val):
            circuit_dict["isource_list"].append(Current_dc_Parsing(val))
        elif VCCS_Regx(val):
            circuit_dict["vccs_list"].append(VCCS_Parsing(val))
        elif VCVS_Regx(val):
            circuit_dict["vcvs_list"].append(VCVS_Parsing(val))
        elif CCCS_Regx(val):
            circuit_dict["cccs_list"].append(CCCS_Parsing(val))
        elif CCVS_Regx(val):
            circuit_dict["ccvs_list"].append(CCVS_Parsing(val))                        
        else:
            pass
            # TODO: Do something notify for error
    circuit_dict["num_nets"] = Get_Number_of_Nets(circuit_dict)
    return circuit_dict
