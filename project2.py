#!/usr/bin/env python3
# Anirudh Agarwala
# Ojas Goyal
# Pasha Pourmand
# Miguel Sanchez

import math
import cmath
import time
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

def fft(poly1, poly2):
	#determine dimension of matrix M
	deg1 = len(poly1) - 1
	deg2 = len(poly2) - 1

	#Find dimension that is greater than deg1 + deg2 and is a power of 2
	dim = deg1 + deg2 + 1
	dim = int(pow(2, math.ceil(math.log(dim,2))))
	print("Dimension of Matrix M is: ", dim)
	
	#determine omega in radians
	w = 360.0/dim
	w = w/180 * cmath.pi

	#Create matrix M
	M = []
	for i in range(dim):
		row = []
		for j in range(dim):
			row.append(cmath.rect(1,i*j*w))
		M.append(row)

	#determine M inverse
	M = np.matrix(M)
	conjM = M.conjugate()

	#Create vector V
	poly1_arr = []
	poly2_arr = []
	for i in range(1,dim+1):
		omega = i*w
		sum = 0
		for j in range(0, len(poly1)):
			sum = sum + poly1[j]*cmath.rect(1,j*omega)
		poly1_arr.append(sum)
		
		sum = 0
		for j in range(0, len(poly2)):
			sum = sum + poly2[j]*cmath.rect(1,j*omega)
		poly2_arr.append(sum)		

	V = []
	for i in range(dim-1, -1, -1):
		V.append([poly1_arr[i]*poly2_arr[i]])	
	
	V = np.matrix(V)
	
	C = np.squeeze(np.asarray(conjM*V))

	temp = []
	temp.append(C[0].real)
	for i in range(dim - 1, 0, -1):
		temp.append(C[i].real/dim)
	C = temp[:(len(poly1)+len(poly2)-1)]

	return C

def main():

  # polynomials represented as coefficients
  polynomial_one = [4,3,10]
  polynomial_two = [4,10]

  t0 = time.clock()
  ans = naive(polynomial_one,polynomial_two)
  print(time.clock() - t0)

  print(ans)

  t0 = time.clock()
  ans2 = fft(polynomial_one, polynomial_two)
  print(time.clock() - t0)

  print(ans2)

if __name__ == '__main__':
  main()
