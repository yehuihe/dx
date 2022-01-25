"""Simulation Class -- Geometric Brownian Motion
"""

# Author: Yehui He <yehui.he@hotmail.com>
# License: Apache-2.0 License

import numpy as np

from .sn_random_numbers import sn_random_numbers
from .simulation_class import SimulationClass


class GeometricBrownianMotion(SimulationClass):
    """Class to generate simulated paths based on
    the Black-Scholes-Merton geometric Brownian motion model.

    Parameters
    ----------
    name : str
        Name of the object.

    mar_env : MarketEnvironment
        Market environment data for simulation.

    corr : bool
        True if correlated with other model object
    """

    def __init__(self, name, mar_env, corr=False):
        super().__init__(name, mar_env, corr)

    def update(self, initial_value=None, volatility=None, final_date=None):
        if initial_value:
            self.initial_value = initial_value
        if volatility:
            self.volatility = volatility
        if final_date:
            self.final_date = final_date
        self.instrument_values = None

    def generate_paths(self, fixed_seed=False, day_count=365.):
        if not self.time_grid.any():
            # method from generic simulation class
            self.generate_time_grid()
        # number of dates for time grid
        M = len(self.time_grid)
        # number of paths
        I = self.paths
        # ndarray initialization for path simulation
        paths = np.zeros((M, I))
        # initialize first date with initial_value
        paths[0] = self.initial_value
        if not self.correlated:
            # if not correlated, generate random numbers
            rand = sn_random_numbers((1, M, I),
                                     fixed_seed=fixed_seed)
        else:
            # if correlated, use random number object as provided
            # in market environment
            rand = self.random_numbers
        short_rate = self.discount_curve.short_rate
        # get short_rate for drift of process
        for t in range(1, len(self.time_grid)):
            # select the right time slice from the relevant
            # random number set
            if not self.correlated:
                ran = rand[t]
            else:
                ran = np.dot(self.cholesky_matrix, rand[:, t, :])
                ran = ran[self.rn_set]
            dt = (self.time_grid[t] - self.time_grid[t - 1]).days / day_count
            # difference between two dates as year fraction
            paths[t] = paths[t - 1] * np.exp((short_rate - 0.5 *
                                              self.volatility ** 2) * dt +
                                              self.volatility * np.sqrt(dt) * ran)
            # generate simulated values for the respective date
        self.instrument_values = paths
