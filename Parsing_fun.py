import os
from typing import List, Dict
import re
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
        "from": resistor_line_split[2],
        "to": resistor_line_split[3],
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
        "from": capacitor_line_split[2],
        "to": capacitor_line_split[3],
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
        "from": inductor_line_split[2],
        "to": inductor_line_split[3],
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
        "from": voltage_dc_line_split[2],
        "to": voltage_dc_line_split[3],
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
        "from": current_dc_line_split[2],
        "to": current_dc_line_split[3],
        "type": current_dc_line_split[4],
        "value": int(current_dc_line_split[5][:-1]) if not current_dc_line_split[5][-1].isdigit() else int(current_dc_line_split[5]),
        "unit": current_dc_line_split[5][-1] if not current_dc_line_split[5][-1].isdigit() else "nothing"
    }
    return dict


def parser(content: str) -> Dict:
    content_without_dashed_lines = []
    circuit_dict = {}
    component_num = 0
    for i, val in enumerate(content):
        if '//' not in val:
            val = val+' ' if i != len(content)-1 else val
            content_without_dashed_lines.append(val)

    for i, val in enumerate(content_without_dashed_lines):
        component_num = f"component_{i}"
        if Resistor_Regx(val):
            circuit_dict[component_num] = Resistor_Parsing(val)
        elif Capacitor_Regx(val):
            circuit_dict[component_num] = Capacitor_Parsing(val)
        elif Voltage_DC_Regx(val):
            circuit_dict[component_num] = Voltage_dc_Parsing(val)
        elif Current_DC_Regx(val):
            circuit_dict[component_num] = Current_dc_Parsing(val)
        elif Inductor_Regx(val):
            circuit_dict[component_num] = Inductor_Parsing(val)
        else:
            print("Nothing")
            pass
            # TODO: Do something notify for error
    return circuit_dict