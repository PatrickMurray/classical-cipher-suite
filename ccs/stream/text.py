#!/usr/bin/env python3
"""
TODO
"""


class TextStream:
    """
    TODO
    """
    def __init__(self, stream):
        """
        TODO
        """

        if type(stream) is str:
            self._stream = list(stream)
        elif stream is None:
            self._stream = []
        elif isinstance(stream, TextStream):
            self._stream = stream
        else:
            raise TypeError('TODO')

        return


    def __iter__(self):
        """
        TODO
        """
        if type(self._stream) is list:
            if 0 < len(self._stream):
                yield self._stream.pop(0)
        elif isinstance(self._stream, TextStream):
            return
        else:
            raise RuntimeError('Unexpected internal error TODO')
        
        return


    def __next__(self):
        """
        TODO
        """
        return 'foobar'


    def __repr__(self):
        """
        TODO
        """
        return


    def __str__(self):
        """
        TODO
        """
        return
