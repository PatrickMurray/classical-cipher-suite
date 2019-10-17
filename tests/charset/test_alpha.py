#!/usr/bin/env python3


import ccs.charset.alpha


def test_alpha_symbols():
    symbols = ccs.charset.alpha.symbols

    assert len(symbols) == 52
    
    for symbol in symbols:
        assert symbol.isalpha()
