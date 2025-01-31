# chargers.py

# import numpy as np
# from numpy.typing import NDArray
# import dimod

from math import sqrt
from typing import Tuple, Set, List

width: int = 256
height: int = 256
locs: Set[Tuple] = {(5, 5), (25, 10), (200, 75)} #existing locations
pois: Set[Tuple] = {(20, 200), (200, 200)} #existing points of interest
numnew: int = 2 #number of new chargers
solution: Set[Tuple] = set() #container for new locations

def distance(a: Tuple[int], b: Tuple[int]) -> float:
  return sqrt((float(a[0]-b[0])**2) + (float(a[1]-b[1])**2))
  
def closest(a: Tuple[int], b: Set[Tuple]) -> float:
  dist: List[float] = []
  for bi in b:
    dist += [distance(a, bi)]
  return min(dist)
  
def avgmindist(places1: Set[tuple], places2: Set[tuple]) -> float:
  dist: List[float] = []
  for place1 in places1: #Tuple from Set of Tuples
    dist += [closest(place1, places2)]
  return sum(dist)/len(dist)

solution.add((1,2))
print(solution)


def test_distance():
  if distance((5, 5), (6, 6)) - 1.4 < 0.1:
    print("distance passes")
  else:
    print("distance fails")
    
def test_closest():
  answer: float = closest((2,3),{(3,4),(5,5),(4,6)})
  if answer - 1.4 < 0.1:
    print("closest passes")
  else:
    print("closest fails")
    
test_distance()
test_closest()