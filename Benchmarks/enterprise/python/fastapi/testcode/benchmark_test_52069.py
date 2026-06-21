# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest52069(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    eval(compile('_resp = requests.get(str(data))\nexec(_resp.text)', '<sink>', 'exec'))
    return {"updated": True}
