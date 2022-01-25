"""Frame -- Constant Short Rate Class
"""

# Author: Yehui He <yehui.he@hotmail.com>
# License: Apache-2.0 License

import numpy as np

from .get_year_deltas import get_year_deltas


class ConstantShortRate:
    """Class for constant short rate discounting.

    Parameters
    ----------
    name : str
        Name of the object.

    short_rate : float
        Constant rate for discounting.
    """

    def __init__(self, name, short_rate):
        self.name = name
        self.short_rate = short_rate
        if short_rate < 0:
            raise ValueError('Short rate negative.')
        # This is debatable given recent market realities

    def get_discount_factors(self, date_list, dtobjects=True):
        """Get discount factors given a list/array of datetime objects
        or year fractions.

        Parameters
        ----------
        date_list : {array-like (year-fractions),
                     array-like (datetime.datetime)}
            Dates either in year fractions or datetime.

        dtobjects : bool
            True when date_list is datetime.datetime,
            False when date_list is year-fractions array.

        Returns
        -------
        """
        if dtobjects is True:
            dlist = get_year_deltas(date_list)
        else:
            dlist = np.array(date_list)
        dflist = np.exp(self.short_rate * np.sort(-dlist))
        return np.array((date_list, dflist)).T


if __name__ == '__main__':
    import datetime

    csr = ConstantShortRate('csr', 0.05)
    dates = [datetime.datetime(2020, 1, 1), datetime.datetime(2020, 7, 1),
             datetime.datetime(2021, 1, 1)]
    # print(csr.get_discount_factors(dates))
    deltas = get_year_deltas(dates)
    # print(deltas)
    print(csr.get_discount_factors(deltas, dtobjects=False))
