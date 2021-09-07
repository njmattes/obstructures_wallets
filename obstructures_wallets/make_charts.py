#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import tanh, pi
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from obstructures_wallets.model.constants import BAND1, BAND2, ALPHA, DECAY
from obstructures_wallets.model.constants import OBJ_WEIGHT, N, ELASTICITY
from obstructures_wallets.model.area import area
from obstructures_wallets.model.modulus import modulus3
from obstructures_wallets.model.objective import objective


matplotlib.style.use('ggplot')


def security(a=.6, b=.5, c=1.55, d=2.55, r=.5):

    def f(x, a=a, r=r):
        return (1 - a) * ((b - x) / b) ** r + a

    def g(x, a=a, r=r):
        return a * ((c - x) / (c - b)) ** r

    def h(x, r=r):
        return (1 - a) * ((x - c) / (d - c)) ** r + a

    xa = np.arange(0, 50) * 1e-2
    xb = np.arange(50, 155) * 1e-2
    xc = np.arange(155, 255) * 1e-2
    ya = np.concatenate((f(xa), g(xb), h(xc)))
    yb = np.concatenate((f(xa, a=.9), g(xb, a=.9), h(xc)))
    yc = np.concatenate((f(xa, r=.3), g(xb, r=.3), h(xc, r=.3)))
    data = dict(one=ya, two=yb, three=yc,)
    xs = np.concatenate((xa, xb, xc))
    df = pd.DataFrame(data, index=xs)
    df.columns=['r=.5, a=.6', 'r=.5, a=.9', 'r=.3, a=.6']
    ax = df.plot(figsize=(8,4))
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig('./security.svg')
    df = pd.DataFrame(ya, index=xs/np.max(xs))
    ax = df.plot(kind='area', figsize=(4,4), color='black')
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig('./security_area.svg')


def stretch(e=5.):

    def f(x, m=1., e=e):
        return (np.tanh(e * x - e / 2.) / 2. + .5) / m

    def g(x):
        return (2 * (3.71 + .15) + 2 * x) / (2.109 * pi) - 1

    xs = np.arange(100) * 1e-2
    data = dict(
        one=f(xs),
        two=f(xs, e=4),
        three=f(xs, e=6)
    )
    df = pd.DataFrame(data, index=xs * 6)
    df.columns=['e=5', 'e=4', 'e=6']
    ax = df.plot(figsize=(8,4))
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig('./elasticity.svg')

    xas = np.arange(0, 100) * 1e-2 * g(.1) / 6
    ys = f(xas) / f(xas[-1])
    df = pd.DataFrame(ys, index=xs)
    ax = df.plot(kind='area', ylim=(0,1), color='black', figsize=(4,4))
    # ax.fill_between(xs, ys, 1)
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig('./elasticity_area.svg')


def parameters():
    rs = np.ones(1000)
    es = np.ones(1000)
    os = np.ones(1000)
    aa = np.ones(1000)
    for i in range(1000):
        rs[i] = DECAY.rvs()
        es[i] = ELASTICITY.rvs()
        os[i] = OBJ_WEIGHT.rvs()
        aa[i] = ALPHA.rvs()
    for d in [rs, es, os, aa]:
        df = pd.DataFrame(d, index=range(1000))
        ax = df.plot(kind='hist', bins=50, figsize=(6, 2))
        plt.ylabel = ''
        fig = ax.get_figure()
        fig.tight_layout()

        fig.savefig('./parameter{}.svg'.format(d.mean()))



if __name__  == '__main__':
    # security()
    # stretch()
    parameters()
    plt.show()
