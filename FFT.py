__author__ = 'Miguel'
import numpy
from cmath import exp, pi

def padExtra(x):

    n = len(x)
    for i in range(0, n):
        x.append(0)
    return x


def fft(x):
    # x is a coefficient vector, from lowest to highest power
    n = len(x)
    d = [0] * (n)
    if n <= 1:
        return x
    even = fft(x[0::2])  # we get every 2 powers, starting at 0(evens)
    odd = fft(x[1::2])  # we get every 2 powers, starting at 1(odds)
    wn = exp(2j * pi / n)
    w = 1
    for k in range(0, n / 2):
        d[k] = even[k] + odd[k] * w
        d[k + n / 2] = even[k] - odd[k] * w
        w = wn * w
    return numpy.array(d)


def polyMult(a,b):
    # Function to multiply polynomials using fft
    fftA = fft(padExtra(a))  # manually padded right now. will have to create a pad function
    fftB = fft(padExtra(b))

    solution = numpy.fft.ifft(numpy.multiply(fftB, fftA)).real
    solution = [int(round(i)) for i in solution]
    finalSolution = [solution[0]]
    finalSolution.extend(solution[len(solution):1:-1])
    return finalSolution

print polyMult([-10, 1, -1, 7], [3, -6, 0, 8])







