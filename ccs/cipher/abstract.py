#!/usr/bin/env python3
"""
TODO
"""


import abc

import ccs.stream.plaintext
import ccs.stream.ciphertext


class AbstractCipher(abc.ABC):
    """
    TODO
    """


    def __init__(self, configuration):
        self.configuration = configuration


    @abc.abstractmethod
    def encipher(self, plaintext: ccs.stream.plaintext.PlaintextStream) -> ccs.stream.ciphertext.CiphertextStream:
        """
	TODO
	"""
        return plaintext


    @abc.abstractmethod
    def decipher(self, ciphertext: ccs.stream.ciphertext.CiphertextStream) -> ccs.stream.plaintext.PlaintextStream:
        """
	TODO
	"""
        return ciphertext
