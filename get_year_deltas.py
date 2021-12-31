"""Frame -- Helper Function
"""

# Author: Yehui He <yehui.he@hotmail.com>
# License: Apache-2.0 License

import numpy as np


def get_year_deltas(date_list, day_count=365.):
    """Return vector of floats with day deltas in year fractions.

    Initial value normalized to zero.

    Parameters
    ----------
    date_list : array-like
        Collection of datetime objects.

    day_count : float, default=365.
        number of days for a year
        (to account for different conventions).

    Returns
    -------
    delta_list : array-like
        Year fractions.
    """
    start = date_list[0]
    delta_list = [(date - start).days / day_count
                  for date in date_list]
    return np.array(delta_list)
