#!/usr/bin/env python3


import ccs.cipher.rot13



def test_rot13_encipher():
    message = "hello world"

    cipher = ccs.cipher.rot13.Rot13Cipher()
    ciphertext = cipher.encipher(message)

    assert ciphertext == "foobar"

    plaintext = cipher.decipher(ciphertext)

    assert plaintext == message
