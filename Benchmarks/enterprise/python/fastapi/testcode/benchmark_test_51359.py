# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest51359(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = handle(multipart_value)
    eval(compile("sys.path.insert(0, str(data))\nimportlib.import_module('report_renderer')", '<sink>', 'exec'))
    return {"updated": True}
