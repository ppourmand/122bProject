#!/usr/bin/env python3
# Anirudh Agarwala
# Ojas Goyal
# Pasha Pourmand
# Miguel Sanchez

import cmath
from random import randint
import time
import numpy as np
from scipy import linalg

def naive(poly1, poly2):


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
    invM = linalg.inv(M)

    #Create vector V
    poly1_arr = []
    for i in range(1,dim+1):
        omega = i*w
        sum = 0
        for j in range(0, len(poly1)):
            sum = sum + poly1[j]*cmath.rect(1,j*omega)
        poly1_arr.append(sum)       

    poly2_arr = []
    for i in range(1,dim+1):
        omega = i*w
        sum = 0
        for j in range(0, len(poly2)):
            sum = sum + poly2[j]*cmath.rect(1,j*omega)
        poly2_arr.append(sum)       
    
    V = []
    for i in range(dim-1, -1, -1):
        V.append([poly1_arr[i]*poly2_arr[i]])   
    
    V = np.matrix(V)

    C =  invM * V
    C = np.squeeze(np.asarray(C))
    
    temp = []
    temp.append(C[0].real)
    for i in range(dim-1, 0, -1):
        temp.append(C[i].real)
    C = temp[:(len(poly1)+len(poly2)-1)]

    
    return C

def generate_poly(degree):

    my_list = []
    for i in range(0,degree):
        coeff = randint(1,999)
        my_list.append(coeff)
    return my_list

def main():

    # polynomials represented as coefficients
    polynomial_one = generate_poly(500)
    polynomial_two = generate_poly(500)

    #print "poly 1:", polynomial_one
    #print "poly 2:", polynomial_two
    start = time.time()
    ans = naive(polynomial_one,polynomial_two)
    print("Time for naive: %s seconds" % (time.time() - start))

    #print "ans1: ", ans
    start = time.time()
    ans2 = fft(polynomial_one, polynomial_two)
    print("Time for FFT: %s seconds" % (time.time() - start))
    #print "ans2: ", ans2

if __name__ == '__main__':
    main()
