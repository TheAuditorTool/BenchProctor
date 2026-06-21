# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import importlib


async def BenchmarkTest17788(request: Request, field: str = Form('')):
    field_value = field
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return {"updated": True}
