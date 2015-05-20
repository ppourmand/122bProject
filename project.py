#!/usr/bin/env python3
# Anirudh Agarwala
# Ojas Goyal
# Pasha Pourmand
# Miguel Sanchez

import cmath
import numpy as np
from scipy import linalg

def naive(poly1, poly2):
  """
  This function multiplies two polynomials of different (or same)
  degrees. It does so naively, ie "foil" method
  """

  result = [0]*(len(poly1)+len(poly2)-1)

  for power1,coeff1 in enumerate(poly1):
    for power2,coeff2 in enumerate(poly2):
        result[power1+power2] += coeff1*coeff2

  return result

#determine if a number is a power of 2
def isPowerOf2(num):
        return num != 0 and ((num & (num - 1)) == 0)

def fft(poly1, poly2):
	#determine dimension of matrix M
	deg1 = len(poly1) - 1
	deg2 = len(poly2) - 1

	#Find dimension that is greater than deg1 + deg2 and is a power of 2
	dim = deg1 + deg2 + 1
	while(True):
		if(isPowerOf2(dim) == 1):
			break
		else:
			dim = dim + 1
	#print("Dimension of Matrix M is: ", dim)
	
	#determine omega
	w = 360/dim
	w = cmath.rect(1,w/180 * cmath.pi)	

	#Create matrix M
	M = []
	for i in range(dim):
		row = []
		for j in range(dim):
			row.append(pow(w,i*j))
		M.append(row)

	#determine M inverse
	M = np.array(M)
	invM = linalg.inv(M)

	#Create matrix V			
		

	#C =  1/dim * M inverse * V
		

	#return C

def main():

  # polynomials represented as coefficients
  polynomial_one = [4,3,10]
  polynomial_two = [4,10]
  ans = naive(polynomial_one,polynomial_two)

  print(ans)
  fft(polynomial_one, polynomial_two)

if __name__ == '__main__':
  main()
