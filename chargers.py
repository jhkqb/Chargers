# chargers.py

# import numpy as np
# import dimod
from math import sqrt
from typing import Tuple, Set, List
# from numpy.typing import NDArray

width: int = 256
height: int = 256
locs: Set[Tuple] = {(5, 5), (25, 10), (200, 75)} #existing locations
pois: Set[Tuple] = {(20, 200), (200, 200)} #existing points of interest
numnew: int = 2 #number of new chargers
solution: Set[Tuple] = set() #container for new locations

def distance(a: Tuple[int], b: Tuple[int]) -> float:
  return sqrt((float(a[0]-b[0])**2) + (float(a[1]-b[1])**2))

solution.add((1,2))

print(solution)


def test_distance():
  if distance((5, 5), (6, 6)) - 1.4 < 0.1:
    print("distance passes")
  else:
    print("distance fails")
    
test_distance()