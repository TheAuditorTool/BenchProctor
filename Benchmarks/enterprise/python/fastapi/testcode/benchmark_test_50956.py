# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import html


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest50956(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    processed = str(data).replace("<script", "")
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return {"updated": True}
