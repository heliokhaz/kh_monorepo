# -*- coding: utf-8 -*-

# …/m_utils/src/m_utils/working_dots.py


import time

def working_dots(n=3, delay=0.3):
    for _ in range(n):
        print(".", end="", flush=True)
        time.sleep(delay)
    print()
