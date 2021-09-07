# -*- coding: utf-8 -*-
from obstructures_wallets.model.constants import CARD_WIDTH


def area(band_1, band_2, alpha, decay_rate):
    a = 0

    # Bottom to band 1
    x0, x1 = 0, band_1
    a += alpha * x1
    a -= alpha * x0 - (
        (1 - alpha) * x1 *
        ((x1 - x0) / x1) ** (decay_rate + 1)
    ) / (decay_rate + 1)

    # Band 1 to 2
    x0, x1 = band_1, band_2
    # area += 0
    a -= (
        alpha * (x0 - band_2) *
        (-(x0 - band_2) / (band_2 - band_1)) ** decay_rate
    ) / (decay_rate + 1)

    # Band 2 to top
    x0, x1 = 0, CARD_WIDTH - band_2
    a += alpha * x1
    a -= alpha * x0 - (
        (1 - alpha) * x1 *
        ((x1 - x0) / x1) ** (decay_rate + 1)
    ) / (decay_rate + 1)

    return a / CARD_WIDTH
