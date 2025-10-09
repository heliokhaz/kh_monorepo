# -*- coding: utf-8 -*-

# m_softdev/src/m_softdev/m_iters.py


def chunkify(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]
