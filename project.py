#!/usr/bin/env python3
# Anirudh Agarwala
# Ojas Goyal
# Pasha Pourmand
# Miguel Sanchez

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
	#create matrix M
	len1 = len(poly1)
	len2 = len(poly2)

	#Find dimension that is greater than len1 + len2 and is a power of 2
	dim = len1 + len2
	while(True):
		if(isPowerOf2(dim) == 1):
			break
		else:
			dim = dim + 1
	
	
	
	

def main():

  # polynomials represented as coefficients
  polynomial_one = [4,3,10]
  polynomial_two = [4,10]
  ans = naive(polynomial_one,polynomial_two)

  print(ans)

if __name__ == '__main__':
  main()
