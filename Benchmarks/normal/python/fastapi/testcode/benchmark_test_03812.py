# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from fastapi import Form
from starlette.responses import JSONResponse
import urllib.request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest03812(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return {"updated": True}
