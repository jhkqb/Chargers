# chargers.py

import numpy as np
import dimod
from typing import Tuple, Set
from numpy.typing import NDArray

width: int = 256
height: int = 256
grid: NDArray[np.float64] = np.zeros((width, height), dtype=np.float64)
elocs: Set[Tuple] = {(5, 5), (25, 10), (200, 75)} #existing locations
numnew: int = 2 #number of new chargers
solution: Set[Tuple] = {}


