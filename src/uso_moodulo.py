import random, sys
from equal import equal
from math import *

l = [('(a*b)**3', 'a**3*b**3'),
    ('a/b','1/(b/a)'),
    ('exp(a+b)','(exp(a))*(exp(b))'),
    ('log10(a**b)','b*log10(a)'),
    ('a-b','-(b-a)'),
    ('(a*b)**4', 'a**4*b**4'),
    ('(a+b)**2', 'a**2+2*a*b+b**2'),
    ('(a+b)*(a-b)','a**2-b**2'),
    ('log10(a*b)','log10(a)+log10(b)'),
    ('a*b', 'e**(log10(a)+log10(b))'),
    ('1/((1/a)+(1/b))','(a*b)/(a+b)'),
    ('a*((sin (b))**2)+((cos (b))**2)','a'),
    ('sinh(a+b)','(exp(a))*(exp(b))-(exp(-a))*(exp(-b))/2'),
    ('tan(a+b)','(sin(a+b))/(cos(a+b))'),
    ('sin(a+b)','(sin(a))*(cos(b))+(cos(a))*(sin(b))')]

if __name__ == '__main__':
  A = float(sys.argv[1])
  B = float(sys.argv[2])
  n = int(sys.argv[3])
  
  for elem in l:
    exp1 = elem[0]
    exp2 = elem[1]
    
    print '%40s %40s %20.1f' %(exp1, exp2, equal(exp1, exp2, A, B, n))