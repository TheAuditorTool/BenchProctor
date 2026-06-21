# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest44938(request: Request):
    path_value = request.path_params.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    eval(compile("sys.path.insert(0, str(data))\nimportlib.import_module('report_renderer')", '<sink>', 'exec'))
    return {"updated": True}
