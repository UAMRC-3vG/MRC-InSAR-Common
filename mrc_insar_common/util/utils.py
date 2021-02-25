#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : utils.py
# Author: Alvin(Xinyao) Sun <xinyao1@ualberta.ca>
# Date  : 25.02.2021

import numpy as np

def wrap(phase):
    """wrap.
    Return wrapped phase value
    Args:
        phase:
    """
    return np.angle(1j*phase)

