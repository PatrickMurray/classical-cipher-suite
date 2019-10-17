#!/usr/bin/env python3
"""
TODO
"""


import abc

import ccs.charset.alpha


default_parameters = {
    'charset': ccs.charset.alpha
}


class AbstractConfiguration(abc.ABC):
    """
    TODO
    """


    def __init__(self, parameters: dict = default_parameters):
        self.parameters = parameters


    def get(self, key: str):
        if key not in self.parameters:
            raise KeyError("Unable to locate key: {}".format(key))

        return self.parameters.get(key)


    def get(self, key: str, value):
        self.parameters[key] = value
