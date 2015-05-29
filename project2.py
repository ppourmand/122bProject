#!/usr/bin/env python3
# Anirudh Agarwala
# Ojas Goyal
# Pasha Pourmand
# Miguel Sanchez

import math
import cmath
from random import randint
import time
import numpy as np
from scipy import linalg


def naive(poly1, poly2):
        len1 = len(poly1)
        len2 = len(poly2)

        py1 = poly1
        py2 = poly2

        dim = len1 + len2

        if(len1 > len2):
                while(len1 != len2):
                        py2.insert(0,0)
                        len2 = len(py2)
        else:
                while(len1 != len2):
                        py1.insert(0,0)
                        len1 = len(py1)

        lst1 = []
        for i in range(0,len(py1)):
                lst1.append(py1[i]*py2[0])
	lst1.reverse()

	secPoly = len(py2)
        for i in range(1,secPoly):

                lst2 = []
                for t in range(0,i):
                        lst2.insert(0,0)

		firstPoly = len(py1)
                for j in range(0, firstPoly):
                        lst2.insert(0,py2[i]*py1[j])

		len1 = len(lst1)
		len2 = len(lst2)
                if(len(lst1) < len(lst2)):
                        while(len(lst1) != len(lst2)):
                                lst1.insert(0,0)
				len1 = len(lst1)
                else:
                        while(len(lst1) != len(lst2)):
                                lst2.insert(0,0)
				len2 = len(lst2)

                sum = []
		#print(lst1,lst2)
                for k in range(0, len2):
                        sum.append(lst1[k] + lst2[k])
                lst1 = sum

        sum.reverse()
        return sum

def fft(poly1, poly2):
    #Find dimension that is greater than deg1 + deg2 and is a power of 2
    dim = len(poly1) + len(poly2) - 1
    dim = int(pow(2, math.ceil(math.log(dim,2))))
    
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
    
    #Determine V
    V = []
    for i in range(dim-1, -1, -1):
        V.append([poly1_arr[i]*poly2_arr[i]])   
    
    V = np.matrix(V)

    #Find the Coefficients of polynomial
    C =  invM * V
    C = np.squeeze(np.asarray(C))

    #Get relevant terms and store in C    
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

    #polynomial_one = [1,2,3]
    #polynomial_two = [2,3,4]

    py_one = polynomial_one
    py_two = polynomial_two

    start = time.time()
    ans = naive(polynomial_one,polynomial_two)
    print("Time for naive: %s seconds" % (time.time() - start))
    #print "ans1: ", ans

    #ans2 = fft([0,0,4,3,10,16,12,13], [4,10,13,15,18,0,12])
    start = time.time()
    ans2 = fft(py_one, py_two)
    print("Time for FFT: %s seconds" % (time.time() - start))
    ans2 = [int(round(elem, 0)) for elem in ans2]
    #print "ans2: ", ans2

    if(ans == ans2):
	print("True")

if __name__ == '__main__':
    main()
