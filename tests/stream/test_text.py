#!/usr/bin/env python3


import ccs.stream.text


def test_textstream():
    stream = ccs.stream.text.TextStream("hello world")

    for character in stream:
        print(character)

    assert False
