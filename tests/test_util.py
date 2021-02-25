import numpy as np
from mrc_insar_common.util import sim 


def test_gen_sim_3d():
    stack_length = 10
    dummy_mr = np.random.rand(300, 300)
    dummy_he = np.random.rand(300, 300)
    unwrap_recon_phase, _, _, _, = sim.gen_sim_3d(dummy_mr, dummy_he, stack_length)
    assert unwrap_recon_phase.shape == [300, 300, 10]
