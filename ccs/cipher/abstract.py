#!/usr/bin/env python3
"""
TODO
"""


import abc


class AbstractCipher(abc.ABC):
    """
    TODO
    """


    def __init__(self, configuration):
        self.configuration = configuration


    @abc.abstractmethod
    def encipher(self, message):
        """
	TODO
	"""
        return message


    @abc.abstractmethod
    def decipher(self, ciphertext):
        """
	TODO
	"""
        return ciphertext
