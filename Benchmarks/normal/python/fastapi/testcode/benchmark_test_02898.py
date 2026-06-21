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

async def BenchmarkTest02898(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
