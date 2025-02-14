# chargerstest.py

import chargers as ch

def test_distance():
  if ch.distance((5, 5), (6, 6)) - 1.4 < 0.1:
    print("distance() passes")
  else:
    print("distance() fails")
  return 0
  
def test_closest():
  answer: float = ch.closest((2,3),{(3,4),(5,5),(4,6)})
  if answer - 1.4 < 0.1:
    print("closest() passes")
  else:
    print("closest() fails")
  return 0
  
def test_avgmindist():
  answer: float = ch.avgmindist({(2,3),(4,4)},{(3,4),(5,5),(4,6)})
  if answer - 1.2 < 0.1:
    print("avgmindist() passes")
  else:
    print("avgmindist() fails")
  return 0
  
def test_guess():
  g: int = ch.guess(5)
  a: bool = 0 <= g < 5
  if a:
    print("guess() passes")
  else:
    print("guess() fails")
  return 0
  
def test_addrandcs():
  s: Set = set()
  ss: Set = ch.addrandcs(s,10,10)
  sss: int = next(iter(ss))[0]
  answer: bool = 0 <= sss < 10
  if answer == True:
    print("addrandcs() passes")
  else:
    print("addrandcs() fails")
  return 0
  
def test_solve():
  w: int = 32
  h: int = 32
  p: Set[Tuple] = {(0,0),(31,0),(0,31),(31,31)}
  pl: int = 20
  it: int = 999
  nn: int = 1
  answer: Set[Tuple] = ch.solve(p, pl, it, w, h, nn)
  a: int = answer.pop()[0]
  if (a == 15) or (a == 16) or (a == 17):
    print("solve() passes")
  else:
    print("solve() fails")
  return 0
  
print()
print("Function tests:") 
test_distance()
test_closest()
test_avgmindist()
test_guess()
test_addrandcs()
test_solve()
