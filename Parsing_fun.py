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
    This Function parse voltage_dc_line to its parameters into dictionary as follow
    dict={"instance_name", "component_type", "from", "to", "type", "value", "unit"}
    """
    voltage_dc_line_split = voltage_dc_line.split()
    dict = {
        "instance_name": voltage_dc_line_split[0],
        "component_type": voltage_dc_line_split[1],
        "from": int(voltage_dc_line_split[2]),
        "to": int(voltage_dc_line_split[3]),
        "type": voltage_dc_line_split[4],
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
        "type": current_dc_line_split[4],
        "value": int(current_dc_line_split[5][:-1]) if not current_dc_line_split[5][-1].isdigit() else int(current_dc_line_split[5]),
        "unit": current_dc_line_split[5][-1] if not current_dc_line_split[5][-1].isdigit() else "nothing"
    }
    return dict


def VCCS_Parsing(vccs_line: str) -> Dict:
    """
    This Function parse current_dc_line to its parameters into dictionary as follow
    dict={"instance_name", "component_type", "from", "to", "type", "value", "unit"}
    """
    vccs_line_split = vccs_line.split()
    dict = {
        "instance_name": vccs_line_split[0],
        "component_type": vccs_line_split[1],
        "from_1": int(vccs_line_split[2]),
        "to_1": int(vccs_line_split[3]),
        "from_2": int(vccs_line_split[4]),
        "to_2": int(vccs_line_split[5]),
        "type": vccs_line_split[6],
        "value": int(vccs_line_split[7][:-1]) if not vccs_line_split[7][-1].isdigit() else int(vccs_line_split[7]),
        "unit": vccs_line_split[7][-1] if not vccs_line_split[7][-1].isdigit() else "nothing"
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
                    "vccs_list": []
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
        else:
            pass
            # TODO: Do something notify for error
    circuit_dict["num_nets"] = Get_Number_of_Nets(circuit_dict)
    return circuit_dict
