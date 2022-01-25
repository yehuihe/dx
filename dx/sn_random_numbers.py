"""Frame -- Random Number Generation
"""

# Author: Yehui He <yehui.he@hotmail.com>
# License: Apache-2.0 License
import numpy as np


def sn_random_numbers(shape, antithetic=True, moment_matching=True,
                      fixed_seed=False):
    """Returns an ndarray object of shape with (pseudo)random numbers
    that are standard normally distributed.

    Parameters
    ----------
    shape : tuple (o, n, m)
        Generation of array with shape (o, n, m).

    antithetic : bool, default=True
        Generation of antithetic variates.

    moment_matching : bool, default=True
        Matching of first and second moments.

    fixed_seed : bool, default=False
        Flag to fix the seed.

    Returns
    -------
    ran: numpy.ndarray
        (o, n, m) array of (pseudo)random numbers.
    """
    if fixed_seed:
        np.random.seed(1000)
    if antithetic:
        ran = np.random.standard_normal(
            (shape[0], shape[1], shape[2] // 2))
        ran = np.concatenate((ran, -ran), axis=2)
    else:
        ran = np.random.standard_normal(shape)
    if moment_matching:
        ran = ran - np.mean(ran)
        ran = ran / np.std(ran)
    if shape[0] == 1:
        return ran[0]
    else:
        return ran
