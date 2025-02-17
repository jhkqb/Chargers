# chargers.py

from sys import argv
from random import randint
from math import sqrt
from typing import Tuple, Set, List

#distance between two tuples, a bi-linear form
def distance(a: Tuple[int, int], b: Tuple[int, int]) -> float:
  return sqrt((float(a[0]-b[0])**2) + (float(a[1]-b[1])**2))
  
#minimum distance between a tuple to a set of tuples
def closest(a: Tuple[int], b: Set[Tuple]) -> float:
  copyb = b.copy()
  mindist: float = distance(a, copyb.pop()) #initial state
  for bi in copyb:
    mindist = min(mindist, distance(a, bi)) #update state
  return mindist
  
#average of the minimum distance between two sets of tuples
#with the first set having a higher or equal cardinality
def avgmindist(places1: Set[tuple], places2: Set[tuple]) -> float:
  dist: List[float] = []
  for place1 in places1: #Tuple from Set of Tuples
    dist += [closest(place1, places2)]
  return sum(dist)/len(dist)
  
#random positive integer up to a maximum
def guess(n: int) -> int:
  return randint(0, n-1)
  
#update state by adding random location
def addrandcs(cs: Set[Tuple], w: int, h: int) -> Set[Tuple]:
  cscopy = cs.copy()
  cscopy.add((guess(w),guess(h)))
  return cscopy
  
def solve(pois, plays, iterations, width, height, numnew):
  copypois: Set[Tuple] = pois.copy()
  i: int; j: int; k: int
  d: float = 0.0
  mindist: float = sqrt((width**2)+(height**2)) #state variable
  ttlocs: Set[Tuple] = set()
  tlocs: Set[Tuple] = set()
  for k in range(plays):
    for j in range(iterations):
      tlocs = set() #refresh state
      for i in range(numnew):
        tlocs = addrandcs(tlocs, width, height) #add a chrging station updatng state
        d = avgmindist(copypois, tlocs) #state variable
        if d < mindist:
           mindist = d #updating state
           ttlocs = tlocs #updating state
  # print(mindist) #used for checking under the hood
  return ttlocs

#monte-carlo technique
if (len(argv) > 1) and (argv[1] == "go"):
  width: int = 32
  height: int = 32
  numnew: int = 1 #number of new chargers
  _pois_ = {(0, 0), (31, 31), (0, 31), (31, 0)} #existing points of interest
  _locs_: Set[Set] = set() #state variable location of charging stations
  plays: int = 30
  iterations: int = 999
  _locs_ = solve(_pois_, plays, iterations, width, height, numnew) #updating state
  print()
  print("Solution:")
  print(_locs_)
  print()
