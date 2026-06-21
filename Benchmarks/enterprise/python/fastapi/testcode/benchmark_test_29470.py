# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest29470(request: Request):
    path_value = request.path_params.get('id', '')
    data = handle(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
