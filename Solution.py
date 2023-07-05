import numpy as np
from typing import List


def Solve_Linear_Matrix(Y: np.ndarray, J: np.ndarray, analysis_type: str) -> List:
    Y = Y[1:len(Y), 1:len(Y)]
    J = J[1:len(J)]
    # print(Y)
    # print("")
    # print(J)
    return np.linalg.solve(Y, J) if analysis_type == "dc" else np.abs(np.linalg.solve(Y, J))
