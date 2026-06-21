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

async def BenchmarkTest06648(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
