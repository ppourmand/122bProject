__author__ = 'Miguel'
import numpy
from cmath import exp, pi


def fft(x):
    # x is a coefficient vector, from lowest to highest power
    n = len(x)
    d = [0] * n
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
    return d

fftA = fft([-10, 1, -1, 7])
fftB = fft([3, -6, 0, 8])

c = []

for a, b in zip(fftA, fftB):
    c.append(a * b)

C = numpy.array(c)
solution = numpy.fft.ifft(C)
print c
test = []
tester = numpy.array([-10, 1, -1, 7])
tester = numpy.fft.fft(tester, 2 * len(tester) - 1)
tester2 = numpy.array([-3, -6, 0, 8])
tester2 = numpy.fft.fft(tester2, 2 * len(tester) - 1)
for a,b in zip(tester,tester2):
    test.append(a * b)
print numpy.fft.ifft(test)







