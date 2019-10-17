#!/usr/bin/env python3


import ccs.charset.qwerty


def test_qwerty_symbols():
    symbols = ccs.charset.qwerty.symbols

    assert len(symbols) == 94
    
    for symbol in symbols:
        assert symbol.isprintable()
