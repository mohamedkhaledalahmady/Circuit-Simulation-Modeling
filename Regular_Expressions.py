from typing import List, Dict
import re


def Resistor_Regx(resistor_line: str) -> bool:
    """
    This Function determine if resistor line match standard of netlist structure or not
    """
    pattern = r"^[A-Z|a-z|_][^\s]*\s+(R|r)esistor\s+\d+\s+\d+\s+\d+(\s*|(M|m|K|k|T|t))\s*$"
    return False if re.match(pattern, resistor_line) == None else True

def Capacitor_Regx(capacitor_line: str) -> bool:
    """
    This Function determine if capacitor line match standard of netlist structure or not
    """
    pattern = r"^[A-Z|a-z|_][^\s]*\s+(C|c)apacitor\s+\d+\s+\d+\s+\d+(\s*|(M|m|U|u|P|p|F|f))\s*$"
    return False if re.match(pattern, capacitor_line) == None else True

def Inductor_Regx(voltage_dc_line: str) -> bool:
    """
    This Function determine if inductor source line match standard of netlist structure or not
    """
    pattern = r"^[A-Z|a-z|_][^\s]*\s+(I|i)nductor\s+\d+\s+\d+\s+\d+(\s*|(M|m|U|u|P|p|F|f))\s*$"
    return False if re.match(pattern, voltage_dc_line) == None else True

def Voltage_DC_Regx(voltage_dc_line: str) -> bool:
    """
    This Function determine if dc-voltage source line match standard of netlist structure or not
    """
    pattern = r"^[A-Z|a-z|_][^\s]*\s+(V|v)source\s+\d+\s+\d+\s+(dc|ac)\s+\d+(\s*|m)\s*$"
    return False if re.match(pattern, voltage_dc_line) == None else True

def Current_DC_Regx(voltage_dc_line: str) -> bool:
    """
    This Function determine if dc-current source line match standard of netlist structure or not
    """
    pattern = r"^[A-Z|a-z|_][^\s]*\s+(I|i)source\s+\d+\s+\d+\s+(dc|ac)\s+\d+(\s*|m)\s*$"
    return False if re.match(pattern, voltage_dc_line) == None else True
