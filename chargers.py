# chargers.py

# import numpy as np
# from numpy.typing import NDArray
# import dimod

from random import randint
from math import sqrt
from typing import Tuple, Set, List

#distance between two tuples, a bi-linear form
def distance(a: Tuple[int], b: Tuple[int]) -> float:
  return sqrt((float(a[0]-b[0])**2) + (float(a[1]-b[1])**2))
  
#minimum distance between a tuple and a set of tuples
def closest(a: Tuple[int], b: Set[Tuple]) -> float:
  mindist: float = distance(a, b.pop()) #initial state
  for bi in b:
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
pois: Set[Tuple] = {(5, 5), (25, 10), (20, 30)} #existing points of interest
numnew: int = 2 #number of new chargers
locs: Set[Tuple] = set() #state variable location of charging stations

#monte-carlo technique
iterations: int = (width*height)**2
locs = addrandcs(locs, width, height) #add a charging station updating state variable

#solution
print()
print("Solution:")
print(locs)
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
    
def test_addrandcs():
  s = set()
  ss = addrandcs(s,10,10)
  sss = next(iter(ss))[0]
  answer = 0 <= sss < 10
  if answer == True:
    print("addrandcs() passes")
  else:
    print("addrandcs() fails")
  return 0
   
print("Function tests:") 
test_distance()
test_closest()
test_avgmindist()
test_addrandcs()
print()