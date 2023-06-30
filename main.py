from typing import List, Dict
import pprint
from File_fun import read_file
from Parsing_fun import parser

pprint.pprint(parser(read_file('Netlist_1.txt', list)))