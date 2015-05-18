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

  # initialize result to how many coefficients will be the result
  result = [0]*(len(poly1)+len(poly2)-1)

  # builds the coefficients
  for o1,i1 in enumerate(poly1):
    for o2,i2 in enumerate(poly2):
        result[o1+o2] += i1*i2

  return result

#def fft():

def main():

  # polynomials represented as coefficients
  polynomial_one = [4,3,10]
  polynomial_two = [4,10]
  ans = naive(polynomial_one,polynomial_two)

  print(ans)

if __name__ == '__main__':
  main()