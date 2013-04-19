import random, sys
from math import *

def equal(exp1, exp2, A, B, n):
  cont = 0
  i = 1
  
  while i<=n:
    a = random.uniform(A, B)
    b = random.uniform(A, B)
    
    if eval(exp1) != eval(exp2):
      cont+=1
    i+=1
    
  porcentaje = cont*100/n
  return porcentaje 
  
if __name__ == '__main__':
  exp1 = (sys.argv[1])
  exp2 = (sys.argv[2])
  A = float(sys.argv[3])
  B = float(sys.argv[4])
  n = int(sys.argv[5])  
  
  print 'El porcentaje de error es del', equal(exp1, exp2, A, B, n)