#!/usr/bin/env python3


import ccs.cipher.rot13



def test_rot13_encipher():
    message = "hello world"

    #configuration = ccs.configuration.

    cipher = ccs.cipher.rot13.Rot13Cipher(None)

    ciphertext = str(cipher.encipher(message))

    print(ciphertext)

    assert ciphertext == "foobar"
