# -*- coding: utf-8 -*-

# m_softdev/src/m_softdev/debug.py

import inspect


def debug_var(var_name: str, value):
    frame = inspect.currentframe().f_back
    print(f"[DEBUG] {frame.f_code.co_name}::{var_name} = {value!r}")
