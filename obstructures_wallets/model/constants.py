# -*- coding: utf-8 -*-
from scipy.stats import *
import numpy as np


BAND1 = (np.arange(4) + 1) * .125
BAND2 = 1.55
HEIGHT = 2.55
WIDTH = 3.71
DEPTH = .05 * 3
ALPHA = norm(.7, .1)
DECAY = norm(.5, .1)

CARD_WIDTH = 2.125
RELAXED = 1.2
ELASTICITY = uniform(4.5, 1)

OBJ_WEIGHT = uniform(.6, .2)

N = 1024 * 1