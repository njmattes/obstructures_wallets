# -*- coding: utf-8 -*-
from math import pi, tanh, log, cosh
from obstructures_wallets.model.constants import HEIGHT, WIDTH, DEPTH


def modulus(band_1):
    def f(x):
        center = 3
        return -(x - center) ** 3 / (x - center) + center
    gap = (band_1 * .5) / HEIGHT
    x = 1.2 * (DEPTH + gap) / DEPTH
    return f(x)


def modulus2(band_1, c=None, d=None):
    gap = (band_1 * .5) / HEIGHT
    # return 1. / (10 * (1-gap)) ** 2
    return (1 - gap) ** 2


def modulus3(band_1, e=5.):
    def f(x, m=1.):
        # x = x / 3 - 1
        # return fabs(x) ** (1 + 1. / e) / x / 2 + .5
        # return 1 / (1 + e ** (-12 * x + 6))
        return tanh(e * x - e / 2) / 2 + .5
        # return (tanh(e * x - e / 2) / 2 + .5) / m

    def f1(x, m=1.):
        # x = x / 3 - 1
        # return (2 * fabs(x) ** (2. + e / e)) / ((e + 2.) / e * x ** 2) + x / 2
        # return log(e ** (6 - 12 * x) + 1) / 12 + x - .5
        # return log(cosh(e * x + e/2)) / (e * 2) + x / 2
        return .5 * log(cosh(.5 * (e - 2 * e * x))) / e + .5 * x
        # return (.5 * e * x + .5 * log(cosh(.5 * (e - 2 * e * x)))) / (e * m)

    x = band_1 / HEIGHT
    s = (2 * (WIDTH + DEPTH) + 2 * x) / (2.109 * pi) - 1
    s /= 6

    x0 = 0
    x1 = s
    a = f1(x1)
    a -= f1(x0)
    a = a * (1 / x1) * (1 / f(x1))
    return a


if __name__ == '__main__':
    print(modulus3(.125))
    print(modulus3(.25))
    print(modulus3(.5))
    print(modulus3(.75))
    print(modulus3(1.))
