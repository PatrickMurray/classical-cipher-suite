#!/usr/bin/env python3
"""
TODO
"""


import ccs.cipher.abstract


class Rot13Cipher(ccs.cipher.abstract.AbstractCipher):
    """
    TODO
    """


    def encipher(self, message: str):
        """
	TODO
	"""
        for character in message:
            print(self.configuration)
            yield character


    def decipher(self, ciphertext: str):
        """
	TODO
	"""
        return ciphertext
