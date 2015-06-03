from numpy import fft as f
import time
import numpy
from random import randint
import matplotlib.pyplot as plt

def roundup_pow2(x):
  """
  Round up to power of 2 (obfuscated and unintentionally faster :).
  """
  while x&(x-1):
    x = (x|(x>>1))+1
  return max(x,1)


def fft_mul(coeff1, coeff2):
  """
  FFT multiply two real polynomials (lowest power coeffs are first).
  """
  d = roundup_pow2(len(coeff1)+len(coeff2)-1)
  c1 = f.fft(list(coeff1) + [0] * (d-len(coeff1)))
  c2 = f.fft(list(coeff2) + [0] * (d-len(coeff2)))
  return list(f.ifft(c1 * c2)[:len(coeff1)+len(coeff2)-1].real)


def naive_mul(coeff1, coeff2):
  """
  Naively multiply two polynomials (lowest power coeffs are first).
  """
  d = len(coeff1)+len(coeff2)-1
  ans = [0] * d
  for i in range(d):
    for j1 in range(len(coeff1)):
      j2 = i-j1
      if 0 <= j2 < len(coeff2):
        ans[i] += coeff1[j1] * coeff2[j2]
  return ans


def eval_poly(coeff, x):
  """
  Evaluate polynomial (lowest power coeffs are first).
  """
  return reduce(lambda a, b: a*x+b, coeff[::-1])

def generate_poly(degree):

    my_list = []
    for i in range(0,degree):
        coeff = 0#randint(0,999)
        my_list.append(coeff)
    return my_list

def test():
  """
  Unit test.
  """
  import random

  degree = []
  naive_times = []
  fft_times = []
  for i in range(200):
    degree.append(i)
    c1 = generate_poly(i)
    c2 = generate_poly(i)
    start_naive = time.time()
    p1 = naive_mul(c1, c2)
    end_naive = time.time()
    p2 = fft_mul(c1, c2)
    end_fft = time.time()
    #assert [abs(p1[i]-p2[i])<1e-8 for i in range(len(p1))].count(0)==0
    #print "p1: ", p1 
    #print "p2: ", p2
    #print "degree: ", i
    #print "time for naive:", end_naive - start_naive
    naive_times.append(end_naive - start_naive)
    fft_times.append(end_fft - end_naive)
    #print "time for fft: ", end_fft - end_naive
  plt.plot(naive_times,'g^', fft_times, 'ro')
  plt.ylim(0,.001)
  plt.xlim(0,100)
  plt.ylabel('time in seconds')
  plt.xlabel('degree of polynomial')
  plt.show()
  #print naive_times
test()