# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest79482(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
