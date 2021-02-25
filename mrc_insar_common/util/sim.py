#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : sim.py
# Author: Alvin(Xinyao) Sun <xinyao1@ualberta.ca>
# Date  : 25.02.2021

import numpy as np
from .utils import wrap


def gen_sim_3d(mr,
               he,
               stack_length,
               bperp_scale=2000.,
               dday_stepmax=4,
               dday_scale=11,
               conv1_scale=-0.0000573803,
               conv1_shift=-0.0110171730107,
               conv2_scale=-0.00073405573,
               conv2_shift=-0.00086772422789899997):
    """gen_sim_3d.
    Generate simulated unwraped recon phase with given mr and he
    Args:
        mr: motion rate with shape [H, W]
        he: height error with shape [H, W]
        stack_length: length of stack size
    """
    ddays = np.random.randint(
        1, dday_stepmax, stack_length) * dday_scale  # shape: [stack_length]
    bperps = (np.random.rand(stack_length) -
              0.5) * bperp_scale  # shape: [stack_length]
    conv1 = np.random.rand() * (conv1_scale) + conv1_shift
    conv2 = np.random.rand() * (conv2_scale) + conv2_shift
    unwrap_recon_phase = conv1 * ddays * (np.expand_dims(
        mr, -1)) + conv2 * bperps * (np.expand_dims(he, -1)
                                    )  # shape: [H, W, stack_length]
    return unwrap_recon_phase, ddays, bperps, conv1, conv2
