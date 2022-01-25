"""Frame -- Market Environment Class
"""

# Author: Yehui He <yehui.he@hotmail.com>
# License: Apache-2.0 License


class MarketEnvironment:
    """Class to model a market environment relevant for valuation.

    Parameters
    ----------
    name : str
        Name of the market environment.

    pricing_date : datetime.datetime
        Date of the market environment.
    """

    def __init__(self, name, pricing_date):
        self.name = name
        self.pricing_date = pricing_date
        self.constants = {}
        self.lists = {}
        self.curves = {}

    def add_constant(self, key, constant):
        """Adds a constant (e.g. model parameter)"""
        self.constants[key] = constant

    def get_constant(self, key):
        """Gets a constant"""
        return self.constants[key]

    def add_list(self, key, list_object):
        """Adds a list (e.g. underlyings)"""
        self.lists[key] = list_object

    def get_list(self, key):
        """Gets a list"""
        return self.lists[key]

    def add_curve(self, key, curve):
        """Adds a market curve (e.g. yield curve)"""
        self.curves[key] = curve

    def get_curve(self, key):
        """Gets a market curve"""
        return self.curves[key]

    def add_environment(self, env):
        """Adds and overwrites whole market environments
        with constants, lists, and curves"""
        # Overwrites existing values, if they exist
        self.constants.update(env.constants)
        self.lists.update(env.lists)
        self.curves.update(env.curves)
