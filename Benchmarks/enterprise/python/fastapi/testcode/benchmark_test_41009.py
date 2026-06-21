# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest41009(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
