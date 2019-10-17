#!/usr/bin/env python3


import ccs.charset.alphanum


def test_alphanum_symbols():
    symbols = ccs.charset.alphanum.symbols

    assert len(symbols) == 62
    
    for symbol in symbols:
        assert symbol.isalnum()
