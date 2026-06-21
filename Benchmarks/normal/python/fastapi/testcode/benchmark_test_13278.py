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

async def BenchmarkTest13278(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
