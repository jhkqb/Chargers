# chargers.py

# import numpy as np
# from numpy.typing import NDArray
# import dimod

from random import randint
from math import sqrt
from typing import Tuple, Set, List

#Globals (because Python does not allow proper encapsulation of mutable vars)
_pois_: Set[Tuple] = set() #existing points of interest
_locs_: Set[Set] = set() #state variable location of charging stations

#distance between two tuples, a bi-linear form
def distance(a: Tuple[int], b: Tuple[int]) -> float:
  return sqrt((float(a[0]-b[0])**2) + (float(a[1]-b[1])**2))
  
#minimum distance between a tuple to a set of tuples
def closest(a: Tuple[int], b: Set[Tuple]) -> float:
  copyb = b.copy()
  mindist: float = distance(a, copyb.pop()) #initial state
  for bi in copyb:
    mindist = min(mindist, distance(a, bi)) #update state
  return mindist
  
#average of the minimum distance between two sets of tuples
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

#initial conditions
width: int = 32
height: int = 32
numnew: int = 2 #number of new chargers
_pois_ = {(5, 5), (3, 11), (10, 10), (20, 20), (10,30)} #existing points of interest

#monte-carlo technique
plays: int = 30
iterations: int = 9999 # or better yet (width*height)**2
mindist: float = sqrt((width**2)+(height**2)) #state variable
_ttlocs_: Set[Tuple] = set()
for k in range(plays):
  for j in range(iterations):
    _tlocs_ = set() #state variable
    for i in range(numnew):
      _tlocs_ = addrandcs(_tlocs_, width, height) #add a chrging station updatng state
      d: float = avgmindist(_pois_, _tlocs_) #state variable
      if d < mindist:
         print(d) 
         mindist = d #updating state
         _ttlocs_ = _tlocs_ #updating state
  _locs_ = _ttlocs_ #updateing state

#solution
print()
print("Solution:")
print(_locs_)
print()

#function tests
def test_distance():
  if distance((5, 5), (6, 6)) - 1.4 < 0.1:
    print("distance() passes")
  else:
    print("distance() fails")
  return 0
    
def test_closest():
  answer: float = closest((2,3),{(3,4),(5,5),(4,6)})
  if answer - 1.4 < 0.1:
    print("closest() passes")
  else:
    print("closest() fails")
  return 0
    
def test_avgmindist():
  answer: float = avgmindist({(2,3),(4,4)},{(3,4),(5,5),(4,6)})
  if answer - 1.2 < 0.1:
    print("avgmindist() passes")
  else:
    print("avgmindist() fails")
  return 0
  
def test_guess():
  g: int = guess(5)
  a: bool = 0 <= g < 5
  if a:
    print("guess() passes")
  else:
    print("guess() fails")
  return 0
    
def test_addrandcs():
  s: Set = set()
  ss: Set = addrandcs(s,10,10)
  sss: int = next(iter(ss))[0]
  answer: bool = 0 <= sss < 10
  if answer == True:
    print("addrandcs() passes")
  else:
    print("addrandcs() fails")
  return 0
   
print("Function tests:") 
test_distance()
test_closest()
test_avgmindist()
test_guess()
test_addrandcs()
print()