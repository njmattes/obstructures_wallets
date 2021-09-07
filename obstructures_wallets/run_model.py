#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from obstructures_wallets.model.constants import BAND1, BAND2, ALPHA, DECAY
from obstructures_wallets.model.constants import OBJ_WEIGHT, N, ELASTICITY
from obstructures_wallets.model.area import area
from obstructures_wallets.model.modulus import modulus3 as modulus
from obstructures_wallets.model.objective import objective


matplotlib.style.use('ggplot')
CSV = os.path.join('output', 'wallet_model-{}.csv'.format(
    datetime.datetime.now()))


def mc():
    dfs = []
    for b in range(len(BAND1)):
        df = pd.DataFrame(np.zeros(N))
        for i in range(N):
            a = area(BAND1[b], BAND2, ALPHA.rvs(), DECAY.rvs())
            m = modulus(BAND1[b], ELASTICITY.rvs())
            df.loc[i, 'area'] = a
            df.loc[i, 'modulus'] = m
            df.loc[i, 'objective'] = objective(a, m, OBJ_WEIGHT.rvs())
        dfs.append(df)

    for df in dfs:
        print(df)
        print(df['objective'].median(),
              df['objective'].mean())

    return dfs


if __name__ == '__main__':
    dfs = mc()
    fig, axes = plt.subplots(nrows=len(dfs), ncols=1, figsize=(6, 8),
                             sharex=True, sharey=True)
    for i, var in enumerate(dfs):
        dfs[i]['objective'].hist(ax=axes[i], bins=50)

    dfs[3].to_csv(CSV)
    plt.show()
